# Explanation: This function reads a text file and replaces the content with the one you enter
# Usage: python3 PyHelp/String/ReplaceSubstringInFile.py android_arm64-v8a.sh /home/dir/Android/Sdk/ndk-build /home/dir/Android/Sdk/ndkr11c
# Requirements: Python3
# Source: https://stackoverflow.com/a/20593644

import fileinput
import sys
 
filename = sys.argv[1]
text_to_search = sys.argv[2]
replacement_text = sys.argv[3]
 
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(text_to_search, replacement_text), end='')
