#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import re
from optparse import OptionParser
from sys import stderr
from sys import stdout


# @return [bool] True:Success False:Failure
def do_command(cmd):
    # Command name
    cmd0 = cmd.split(" ")[0]

    # Execute command
    print("> " + cmd)
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=(os.name != 'nt'))
        output = p.communicate()[0].decode("utf-8")
        result = p.returncode
        if result == 127:
            stderr.write("Error: %s command not found.\n" % cmd0)
            sys.exit(1)
        print(output)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            stderr.write("Error: %s command not found.\n" % cmd0)
        else:
            stderr.write("OSError: %s\n" % e)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            stderr.write("Error: %s command not found.\n" % cmd0)
        else:
            stderr.write("OSError: %s\n" % e)
        sys.exit(1)

    # Check return code
    if result != 0:
        return False

    # Check error of output
    error_info = ""
    for line in output.split("\n"):
        if "Failure" in line:
            return False

    # No error
    return True

# @return [string] command output
def do_command_silently(cmd):
    # Command name
    cmd0 = cmd.split(" ")[0]

    # Execute command
    try:
        output = subprocess.check_output(cmd, shell=(os.name != 'nt')).decode("utf-8")
        if cmd0 == "aapt" and "It appears you do not have" in output:
            stderr.write(
                ("Error: aapt error as follows.\n" +
                "--------------------------------------------------\n" +
                "%s\n" +
                "--------------------------------------------------\n\n") % output.rstrip())
            sys.exit(1)
        return output
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            stderr.write("Error: %s command not found.\n" % cmd0)
        else:
            stderr.write("OSError: %s\n" % e)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            stderr.write("Error: %s command not found.\n" % cmd0)
        else:
            stderr.write("OSError: %s\n" % e)
        sys.exit(1)
    except SystemExit as e:
        sys.exit(1)
    except:
        stderr.write("Error: %s\n" % str(sys.exc_info()))
        sys.exit(1)
