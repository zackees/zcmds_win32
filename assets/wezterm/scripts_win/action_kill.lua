-- action_kill.lua
local M = {}

local function kill_foreground(window, pane, wezterm)
  if not (wezterm.target_triple and wezterm.target_triple:find("windows")) then
    if window and window.toast_notification then
      window:toast_notification("WezTerm", "Kill is Windows-only (uses taskkill).", nil, 2500)
    end
    return
  end

  local info = pane:get_foreground_process_info()
  local pid = info and info.pid
  if pid then
    if window and window.toast_notification then
      window:toast_notification("WezTerm", ("Killing PID %d ..."):format(pid), nil, 1500)
    end
    -- Run asynchronously so the UI never blocks
    wezterm.background_child_process({ "taskkill", "/PID", tostring(pid), "/T", "/F" })
  else
    if window and window.toast_notification then
      window:toast_notification("WezTerm", "No foreground PID to kill.", nil, 2000)
    end
  end
end

function M.apply(config, wezterm)
  config.keys = config.keys or {}
  table.insert(config.keys, {
    key = 'K',
    mods = 'CTRL|SHIFT',
    action = wezterm.action_callback(function(window, pane)
      kill_foreground(window, pane, wezterm)
    end),
  })
end

return M
