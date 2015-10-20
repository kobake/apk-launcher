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
# Check apk existence
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
apk_path = os.path.abspath(apk_path)
if not os.path.isfile(apk_path):
    stderr.write('Error: "%s" not found.\n' % apk_path)
    sys.exit(1)


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# chdir
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# apk informations
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
print ""
print "-------- apk informations --------"

print "apk_path = " + apk_path

try:
    package_name = subprocess.check_output('python apk_packagename.py "%s"' % apk_path, shell=True).rstrip()
    print "package_name = " + package_name

    activity_name = subprocess.check_output('python apk_activityname.py "%s"' % (apk_path), shell=True).rstrip()
    print "activity_name = " + activity_name

except SystemExit as e:
    sys.exit(1)

except:
    # stderr.write("Error: %s\n" % str(sys.exc_info()))
    sys.exit(1)

print ""


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# install and execute
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
try:
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    # Install apk
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    # Install
    print "-------- install --------"
    result = command_util.do_command('adb install -r "%s"' % apk_path)

    # If installation failure
    if not result:
        # Uninstall
        print "-------- uninstall --------"
        command_util.do_command('adb uninstall %s' % package_name)

        # Re install
        print "-------- re-install --------"
        command_util.do_command('adb install "%s"' % apk_path)

    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    # Execute apk
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    print "-------- start --------"
    command_util.do_command('adb shell am start -n %s/%s' % (package_name, activity_name))

except SystemExit as e:
    sys.exit(1)

except:
    stderr.write("Error: %s\n" % str(sys.exc_info()))
    sys.exit(1)
