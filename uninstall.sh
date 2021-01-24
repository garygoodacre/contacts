#!/bin/bash

# exit on error
set -euo pipefail

# make sure we're in the right place
cd "$(dirname "$(readlink -fn "$0")")"

# what's the target desktop file we're creating
export TARGET=~/.local/share/applications/contacts.desktop

# remove the target
rm "$TARGET"

# tell the user we did it
echo "Desktop file removed: $TARGET"
