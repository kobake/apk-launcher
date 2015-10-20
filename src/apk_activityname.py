#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Usage: python apk_launcher.py <apk file>
#
import sys
import os
import commands
import subprocess
import re
import command_util
from optparse import OptionParser
from sys import stderr
from sys import stdout

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# command line arguments
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
apk_path = sys.argv[1]
if not apk_path:
    stderr.write("Usage: python %s <apk file>\n" % sys.argv[0])
    sys.exit(1)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# apk path
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
apk_path = os.path.abspath(apk_path)
if not os.path.isfile(apk_path):
    stderr.write('Error: "%s" not found.\n' % apk_path)
    sys.exit(1)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# apk information
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
try:
    # activity name
    activity_name = ""
    output = command_util.do_command_silently('aapt d badging "%s"' % apk_path)
    r = re.compile("launchable-activity: name='([^']+)'")
    for line in output.split("\n"):
        m = r.search(line)
        if m:
            activity_name = m.group(1)
    if(activity_name):
        stdout.write(activity_name)
    else:
        stderr.write("Error: No activity name found.\n")
        sys.exit(1)

except SystemExit as e:
    sys.exit(1)

except:
    stderr.write("Error: %s\n" % str(sys.exc_info()))
    sys.exit(1)
