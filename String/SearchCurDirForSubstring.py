# Explanation: This function searches a substring in files and directories at or higher level then current one
# Usage: python3 SearchCurDirForSubstring.py '/any/dir/or/substring'
# Requirements: Python3 or Python2, grep
# Source: ~

import sys
import subprocess
 
substring = sys.argv[1]

add_wildcard_to_substring = " '.*" + substring + ".*'"

cmd = "grep -nrw . -e" + add_wildcard_to_substring

p = subprocess.Popen(cmd,
                     shell=True)

p.communicate()
