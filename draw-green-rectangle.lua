/c
local AREA = {
    left_top     = { x = 75, y = 172 },
    right_bottom = { x =  88, y = 177 }
}

local player = game.player
local surface = player.surface
rendering.draw_rectangle({
    color        = { r = 0, g = 1, b = 0, a = 0.5 },
    left_top     = AREA.left_top,
    right_bottom = AREA.right_bottom,
    width        = 4,
    surface      = player.surface,
    time_to_live = 600,
    players      = { player }
})