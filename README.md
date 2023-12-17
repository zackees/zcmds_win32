# zcmds_win32

[![Linting](https://github.com/zackees/zcmds_win32/actions/workflows/lint.yml/badge.svg)](https://github.com/zackees/zcmds_win32/actions/workflows/lint.yml)
[![Win_Tests](https://github.com/zackees/zcmds_win32/actions/workflows/push_win.yml/badge.svg)](https://github.com/zackees/zcmds_win32/actions/workflows/push_win.yml)

Optional zcmds package for win32 to make it feel more like a linux distribution. This is a great package to use if you want to
use things like `tee`, `grep` and unix commands and have it work on windows.

# Commands

  * cat
  * cp
  * du
  * git-bash
  * grep
  * home
  * false
  * id
  * ls
  * md5sum
  * mv
  * nano
  * pico
  * ps
  * open
  * rm
  * true
  * test
  * tee
  * touch
  * unzip
  * which
  * wc
  * xargs
  * uniq
  * uname
  * fixvmmem
    * If CPU consumption for vmmem high, run this command to fix it.
  * yes


# Install (normal)
  * `python -m pip install zcmds`


# Install (dev):

  * `git clone https://github.com/zackees/zcmds_win32`
  * `cd zcmds_win32`
  * `python -pip install -e .`


# Release Notes

  * 1.2.4: Fixes `open` when passing in a '.' directory.
  * 1.2.3: `home` now works in non C: drive
  * 1.2.2: Adds `make` tool for building code.
  * 1.2.1: Adds tool `dig`
  * 1.0.26: When sublime is opened via `open` it now opens in it's own window.
  * 1.0.25: Fix `open` for python 3.9
  * 1.0.24: Add `sed`
  * 1.0.23: Yank 1.0.21/22
  * 1.0.20: Adds `uniq` and `uname`
  * 1.0.19: Change default text editor to sublime over textpad
  * 1.0.18: Adds `true` and `false` and `timeout`
  * 1.0.17: Minor fixes.
  * 1.0.16: Adds `xargs`, `ps`, `id`, `wc`, `md5sum`, `tee`
  * 1.0.15: fixed 'no' command, which doesn't exist.
  * 1.0.13: Adds `yes`
  * 1.0.12: open tries to find a text editor.
  * 1.0.11: Adds `sudo_win32[sudo]`
  * 1.0.10: Fixes `fixvmmem` which now uses elevated_exec
  * 1.0.9: Fixes `open` when using forward slashes
  * 1.0.8: Fixes `open` when using `open .`
  * 1.0.7: Fixes missing `fixvmmem`
  * 1.0.5: `open` now assumes current directory if no path is given
  * 1.0.4: `fixvmmem` now runs in elevated privledges
  * 1.0.3: Adds `fixvmmem`
  * 1.0.2: Adds `unzip`
  * 1.0.1: Adds `pico/nano`
  * 1.0.0: Moved zcmds_win32 from zcmds
