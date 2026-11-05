local mod = {}

chronicle.action(
    "custom_gilda",
    "Custom Gilda",
    "Enter an amount to add to your Gilda balance.",
    function(world)
        local amount = tonumber(chronicle.get("custom_gilda_amount")) or 0

        if amount < 1 or amount > 65535 then
            return
        end

        local remaining = amount

        while remaining > 0 do
            local chunk = math.min(remaining, 32767)
            chronicle.add_money(chunk)
            remaining = remaining - chunk
        end
    end
)

-- Each registration is a direct action in the same flat menu.
-- Capture each character in this function so callbacks keep their own ID.
local function register_character(id, key, name)
    chronicle.action(key .. "_hp", name .. " - HP", "Set " .. name .. "'s maximum HP (1-32767). Requires a joined character; does not heal.", function(world)
        local value = tonumber(chronicle.get(key .. "_hp_amount"))
        if value and value >= 1 and value <= 32767 then
            chronicle.call("player.max_hp_set", {character = id, max_hp = math.floor(value)})
        end
    end)

    chronicle.action(key .. "_def", name .. " - DEF", "Set " .. name .. "'s defense (0-32767). Requires a joined character.", function(world)
        local value = tonumber(chronicle.get(key .. "_def_amount"))
        if value and value >= 0 and value <= 32767 then
            chronicle.call("player.defense_set", {character = id, defense = math.floor(value)})
        end
    end)
end

register_character(0, "toan", "Toan")
register_character(1, "xiao", "Xiao")
register_character(2, "goro", "Goro")
register_character(3, "ruby", "Ruby")
register_character(4, "ungaga", "Ungaga")
register_character(5, "osmond", "Osmond")

return mod
