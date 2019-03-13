# Explanation: This function searches for filenames in files and directories at or higher level then current one
# Usage: python3 SearchCurDirForFilename.py '*.so'
# Requirements: Python3 or Python2, linux find
# Source: ~

import sys
import subprocess
 
substring_of_filename = sys.argv[1]

cmd = "find . -name " + substring_of_filename

p = subprocess.Popen(cmd,
                     shell=True)

p.communicate()
