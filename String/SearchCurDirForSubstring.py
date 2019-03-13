# Explanation: This function reads a text file and replaces the content with the one you enter
# Usage: python3 PyHelp/String/SearchCurDirForSubstring.py /any/dir/or/substring
# Requirements: Python3 or Python2, grep
# Source: ~

import sys
import subprocess
 
substring = sys.argv[1]

add_wildcard_to_substring = " '.*" + substring + ".*'"

cmd = "grep -nrwi . -e" + add_wildcard_to_substring

p = subprocess.Popen(cmd,
                     shell=True)

p.communicate()
