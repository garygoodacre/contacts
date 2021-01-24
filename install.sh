#!/bin/bash

# exit on error
set -euo pipefail

# make sure we're in the right place
cd "$(dirname "$(readlink -fn "$0")")"

# what's the target desktop file we're creating
export TARGET=~/.local/share/applications/contacts.desktop

# write the destop file
echo "[Desktop Entry]
Version=1.1
Name=Contacts
Comment=Contacts
Exec=$(pwd)/dist/contacts
Path=$(pwd)/dist/
Icon=$(pwd)/VIEW.ICO
Terminal=false
Type=Application
Categories=Utility;Application;" > "$TARGET"

# make it executable
chmod +x "$TARGET"

# tell the user we did it
echo "Desktop file created: $TARGET"
