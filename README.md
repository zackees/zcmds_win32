# zcmds_win32

Optional zcmds package for win32 to make it feel more like a linux distribution.

# Commands

  * cat
  * cp
  * du
  * git-bash
  * grep
  * home
  * ls
  * mv
  * open
  * rm
  * test
  * touch
  * unzip
  * which
  * nano
  * pico
  * fixvmmem
    * If CPU consumption for vmmem high, run this command to fix it.
  * yes


# Install (normal)
  * `python -pip install zcmds`


# Install (dev):

  * `git clone https://github.com/zackees/zcmds_win32`
  * `cd zcmds_win32`
  * `python -pip install -e .`


# Release Notes
  * 1.0.14: Adds `no`
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
