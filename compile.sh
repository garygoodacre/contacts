#!/bin/bash

# exit on error
set -euo pipefail

# make sure we're in the right place
cd "$(dirname "$(readlink -fn "$0")")"

# clean up
rm -rf ./dist/*

# build the python app
~/.local/bin/pyinstaller -F -w ./contacts.py

# tell the user we did it
echo 'Compiled! To install a launcher run: ./install.sh'
