-- rc_right_click.lua
local M = {}

function M.apply(config, wezterm)
  local act = wezterm.action

  local function right_click_paste_action(window, pane)
    local has_selection = window:get_selection_text_for_pane(pane) ~= ""
    if has_selection then
      window:perform_action(act.CopyTo("ClipboardAndPrimarySelection"), pane)
      window:perform_action(act.ClearSelection, pane)
    else
      window:perform_action(act({ PasteFrom = "Clipboard" }), pane)
    end
  end

  config.mouse_bindings = config.mouse_bindings or {}
  table.insert(config.mouse_bindings, {
    event = { Down = { streak = 1, button = "Right" } },
    mods  = "NONE",
    action = wezterm.action_callback(right_click_paste_action),
  })
end

return M
