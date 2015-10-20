#!/bin/bash

if [ "$1" == "" ]; then
    echo Usage: apk_launcher.sh \<apk file\> >&2
    exit 1
fi

# check python command existence
if hash python 2>/dev/null; then
    # python found.
    :
else
    # python not found.
    echo Error: python command not found. >&2
    exit 1
fi

# launch python script
SCRIPT_DIR=`dirname $0`
python "${SCRIPT_DIR}/src/apk_launcher.py" "$1"

