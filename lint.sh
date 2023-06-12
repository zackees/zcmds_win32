#!/bin/bash
set -e
# cd to self bash script directory
cd $( dirname ${BASH_SOURCE[0]})
echo Running isort
isort --profile black zcmds_win32
echo Running black
black zcmds_win32
echo Running flake8 zcmds_win32
flake8 zcmds_win32
echo Running pylint zcmds_win32
pylint zcmds_win32
echo Running mypy zcmds_win32
mypy zcmds_win32
echo Linting complete!