-- wezterm.lua
local wezterm = require 'wezterm'

local config = {}

-- Load modules (files must be in same directory as this file)
require('shell_gitbash').apply(config, wezterm)     -- choose Git Bash as default shell if found
require('rc_right_click').apply(config, wezterm)    -- right-click paste/copy behavior
require('action_kill').apply(config, wezterm)       -- async kill foreground process (Ctrl+Shift+K)

-- Add any other global settings here...
-- e.g., config.font = wezterm.font("JetBrains Mono")

return config
