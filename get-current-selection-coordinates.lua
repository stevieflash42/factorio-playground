/c
local sel = game.player.selected
if sel then
    local pos = sel.position
    local width = sel.tile_width
    local height = sel.tile_height
    game.print(math.floor(pos.x) .. ", " .. math.floor(pos.y))
    game.print(math.floor(pos.x + height) .. ", " .. math.floor(pos.y + width))
else
    game.print("Hover over an entity first")
end