/c
local LOADER_NAME = "stack-mdrn-loader"
local INSERTER_NAME = "stack-inserter"
local INSERTER_QUALITY = "legendary"
local AREA = nil

local DIR_AXIS_OFFSET = { [0] = { x = 0, y = -1 }, [4] = { x = 1, y = 0 }, [8] = { x = 0, y = 1 }, [12] = { x = -1, y = 0 } }
local PICKUP_DIR = { [0] = { x = 0, y = -1 }, [4] = { x =  1, y = 0 }, [8] = { x = 0, y =  1 }, [12] = { x = -1, y = 0 } }
local DROP_DIR   = { [0] = { x = 0, y =  1 }, [4] = { x = -1, y = 0 }, [8] = { x = 0, y = -1 }, [12] = { x =  1, y = 0 } }
local LOADER_DIR_TO_INSERTER_DIR_MAP = { [0] = 8, [4] = 12, [8] = 0, [12] = 4 }

local function pos_key(pos) return pos.x .. "," .. pos.y end

local function set_hand_positions(inserter, pickup_dist, drop_dist)
    local dir = inserter.direction
    local p = PICKUP_DIR[dir]
    local d = DROP_DIR[dir]
    if not p or not d then return end
    inserter.pickup_position = { x = inserter.position.x + p.x * pickup_dist, y = inserter.position.y + p.y * pickup_dist }
    inserter.drop_position   = { x = inserter.position.x + d.x * drop_dist,   y = inserter.position.y + d.y * drop_dist }
    inserter.direction = inserter.direction
end

local function replace_single_loader(loader, surface, paired_type)
    if not loader.valid then return nil end
    local pos = loader.position
    local direction = LOADER_DIR_TO_INSERTER_DIR_MAP[loader.direction]
    local force = loader.force
    local saved_connections = {}
    local connectors = loader.get_wire_connectors(false)
    if connectors then
        for connector_id, connector in pairs(connectors) do
            for _, conn in ipairs(connector.connections) do
                if conn.target.owner ~= loader then
                    table.insert(saved_connections, { connector_id = connector_id, target = conn.target })
                end
            end
        end
    end
    local saved_cb = nil
    local cb = loader.get_control_behavior()
    if cb then
        saved_cb = {
            circuit_condition = cb.circuit_condition,
            circuit_enable_disable = cb.circuit_enable_disable,
            logistic_condition = cb.logistic_condition,
            connect_to_logistic_network = cb.connect_to_logistic_network,
            circuit_set_filters = cb.circuit_set_filters,
        }
    end
    local saved_filters = {}
    local saved_filter_mode = nil
    local filter_count = loader.filter_slot_count
    if filter_count and filter_count > 0 then
        saved_filter_mode = loader.loader_filter_mode
        for i = 1, filter_count do
            local f = loader.get_filter(i)
            if f then saved_filters[i] = f end
        end
    end
    loader.destroy()
    local inserter = surface.create_entity({ name = INSERTER_NAME, position = pos, direction = direction, force = force, quality = INSERTER_QUALITY })
    if not inserter then
        game.print("[StackLoader Replace] Failed to create inserter at " .. serpent.line(pos))
        return nil
    end
    if saved_cb then
        local dst_cb = inserter.get_or_create_control_behavior()
        if dst_cb then
            if saved_cb.circuit_condition then dst_cb.circuit_condition = saved_cb.circuit_condition end
            if saved_cb.circuit_enable_disable then dst_cb.circuit_enable_disable = saved_cb.circuit_enable_disable end
            if saved_cb.logistic_condition then dst_cb.logistic_condition = saved_cb.logistic_condition end
            if saved_cb.connect_to_logistic_network then dst_cb.connect_to_logistic_network = saved_cb.connect_to_logistic_network end
            if saved_cb.circuit_set_filters then dst_cb.circuit_set_filters = saved_cb.circuit_set_filters end
        end
    end
    local dst_connectors = inserter.get_wire_connectors(false)
    if dst_connectors then
        for _, saved in ipairs(saved_connections) do
            local dst_connector = dst_connectors[saved.connector_id]
            if dst_connector and saved.target.valid then dst_connector.connect_to(saved.target) end
        end
    end
    if next(saved_filters) then
        inserter.use_filters = true
        if saved_filter_mode and saved_filter_mode ~= "none" then inserter.inserter_filter_mode = saved_filter_mode end
        for i, filter in pairs(saved_filters) do
            inserter.set_filter(i, filter)
        end
    end
    if paired_type == "input" then
        set_hand_positions(inserter, 1, 2)
    elseif paired_type == "output" then
        set_hand_positions(inserter, 2, 1)
    end
    return inserter
end

local replaced_count = 0
for _, surface in pairs(game.surfaces) do
    local loaders = surface.find_entities_filtered({ name = LOADER_NAME, area = AREA,  })
    local loader_map = {}
    for _, loader in ipairs(loaders) do loader_map[pos_key(loader.position)] = loader end
    local processed = {}
    for _, loader in ipairs(loaders) do
        if not loader.valid then goto continue end
        local key = pos_key(loader.position)
        if processed[key] then goto continue end
        local direction = loader.direction
        local offset = DIR_AXIS_OFFSET[direction]
        if not offset then
            game.print("[StackLoader Replace] Unknown direction " .. direction .. " at " .. serpent.line(loader.position))
            goto continue
        end
        local nkey = (loader.position.x + offset.x) .. "," .. (loader.position.y + offset.y)
        local neighbor = loader_map[nkey]
        if not neighbor then
            nkey = (loader.position.x - offset.x) .. "," .. (loader.position.y - offset.y)
            neighbor = loader_map[nkey]
        end
        if neighbor and not processed[nkey] and neighbor.valid and neighbor.direction == direction then
            local input_loader, output_loader
            if loader.loader_type == "input" then
                input_loader = neighbor
                output_loader = loader
            else
                input_loader = loader
                output_loader = neighbor
            end
            processed[key] = true
            processed[nkey] = true
            local input_inserter  = replace_single_loader(input_loader,  surface, "input")
            local output_inserter = replace_single_loader(output_loader, surface, "output")
            if input_inserter  then replaced_count = replaced_count + 1 end
            if output_inserter then replaced_count = replaced_count + 1 end
        else
            processed[key] = true
            local inserter = replace_single_loader(loader, surface, nil)
            if inserter then replaced_count = replaced_count + 1 end
        end
        ::continue::
    end
end
game.print("[StackLoader Replace] Done. Replaced " .. replaced_count .. " stack loaders with legendary stack inserters.")