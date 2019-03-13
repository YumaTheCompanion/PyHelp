# Explanation: This function downloads the websites in text format
# Usage: python3 PyHelp/Web/DownloadWebPages.py https://github.com/YumaTheCompanion
# Requirements: Python3 or Python2, lynx
# Source: ~

import subprocess
import sys
import datetime

argvLen = len(sys.argv)

for filename in sys.argv[1:argvLen]:
