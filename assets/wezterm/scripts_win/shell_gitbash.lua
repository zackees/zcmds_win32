-- shell_gitbash.lua
local M = {}

-- split stdout to lines
local function split_lines(s)
  local t = {}
  for line in string.gmatch(s or "", "[^\r\n]+") do
    table.insert(t, line)
  end
  return t
end

-- run `where.exe thing` and return a list of matches, or {}
local function where_all(wezterm, thing)
  local ok, stdout, _ = wezterm.run_child_process({ "where.exe", thing })
  if not ok then return {} end
  return split_lines(stdout)
end

-- test if a file exists by asking where.exe to /Q it
local function path_exists(wezterm, p)
  if not p or p == "" then return false end
  local ok, _, _ = wezterm.run_child_process({ "where.exe", "/Q", p })
  return ok
end

-- aggressive search for Git for Windows bash.exe (console app)
local function resolve_git_bash_exe(wezterm)
  -- 1) PATH hits: prefer Git-for-Windows flavor
  for _, hit in ipairs(where_all(wezterm, "bash.exe")) do
    if hit:match([[\Git\bin\bash%.exe$]]) then
      return hit
    end
  end

  -- 2) Known install roots
  local pf  = os.getenv("ProgramFiles")
  local pfx = os.getenv("ProgramFiles(x86)")
  local lad = os.getenv("LOCALAPPDATA")
  local candidates = {
    pf and (pf .. [[\Git\bin\bash.exe]]) or nil,
    pfx and (pfx .. [[\Git\bin\bash.exe]]) or nil,
    lad and (lad .. [[\Programs\Git\bin\bash.exe]]) or nil,
  }
  for _, p in ipairs(candidates) do
    if path_exists(wezterm, p) then return p end
  end

  -- 3) git-bash.exe on PATH -> derive bin\bash.exe next to it
  for _, hit in ipairs(where_all(wezterm, "git-bash.exe")) do
    local base = hit:gsub([[git%-bash%.exe$]], "bin\\bash.exe")
    if path_exists(wezterm, base) then
      return base
    end
  end

  return nil
end

function M.apply(config, wezterm)
  if not (wezterm.target_triple and wezterm.target_triple:find("windows")) then
    return
  end

  -- toggle to run via cmd.exe /K "bash -l -i" instead of exec bash directly
  local USE_CMD_WRAPPER = false

  local bash = resolve_git_bash_exe(wezterm)
  if bash then
    if USE_CMD_WRAPPER then
      config.default_prog = { "cmd.exe", "/K", string.format('"%s" -l -i', bash) }
    else
      config.default_prog = { bash, "-l", "-i" }
    end

    -- optional: add to launch menu
    config.launch_menu = config.launch_menu or {}
    table.insert(config.launch_menu, { label = "Git Bash", args = { bash, "-l", "-i" } })
  else
    wezterm.log_warn("Git Bash not found; leaving default shell unchanged.")
  end
end

return M
