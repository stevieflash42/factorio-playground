/c
local single_train_id = nil
for _, train in pairs(game.train_manager.get_trains({})) do
  if single_train_id == nil or train.id == single_train_id then
    local schedule = train.get_schedule()
    if schedule then
      local replaced = 0
      for i = 1, schedule.get_record_count() do
        local record = schedule.get_record{ schedule_index = i }
        if record and record.station then
          local station_lower = string.lower(record.station)
          local is_drop = string.find(station_lower, "drop")
          local is_pickup = string.find(station_lower, "pick")

          if is_drop or is_pickup then
            local conditions = schedule.get_wait_conditions{ schedule_index = i }
            if conditions and #conditions == 1 then
              local cond = conditions[1]
              if cond.type == "time" and (cond.ticks == 300 or cond.ticks == 180) then
                local new_type = is_drop and "empty" or "full"
                schedule.change_wait_condition({ schedule_index = i }, 1, { type = new_type, compare_type = cond.compare_type })
                game.print("[REPLACED] Train #" .. tostring(train.id) .. " stop '" .. record.station .. "' -> " .. new_type)
                replaced = replaced + 1
              else
                game.print("[SKIP] Train #" .. tostring(train.id) .. " stop '" .. record.station .. "' no match (type=" .. tostring(cond.type) .. " ticks=" .. tostring(cond.ticks) .. ")")
              end
            elseif conditions and #conditions > 1 then
              game.print("[SKIP] Train #" .. tostring(train.id) .. " stop '" .. record.station .. "' has " .. #conditions .. " conditions, leaving untouched")
            else
              game.print("[SKIP] Train #" .. tostring(train.id) .. " stop '" .. record.station .. "' has no conditions")
            end
          end
        end
      end
      game.print("Train #" .. tostring(train.id) .. " done. Replaced " .. replaced .. " condition(s).")
    end
  end
end