# Explanation: This function downloads the websites in text format
# Usage: python3 PyHelp/Web/DownloadWebPages.py https://github.com/YumaTheCompanion
# Requirements: Python3 or Python2, lynx
# Source: ~

import subprocess
import sys
import datetime

argvLen = len(sys.argv)

for website in sys.argv[1:argvLen]:
	filename = website.split('/')
	filenameText = filename[len(filename) - 1] + '.txt'
	filenameErr = filename[len(filename) - 1] + '_err.txt'
	
	with open(filenameText, "w") as out, open(filenameErr, "w") as err:
		out.write("Date: " + str(datetime.datetime.now()))
		out.write("\r\n")
		out.write("==========")
		err.write("Date: " + str(datetime.datetime.now()))
		err.write("\r\n")
		err.write("==========")
		p = subprocess.Popen(["lynx", website, "-dump", "-nolist", " >> ", filenameText, "2>&1"], stdout=out, stderr=err)
		
		p.communicate()[0]
