# Explanation: This function reads a text file and replaces the content with the one you enter
# Usage: python3 ReplaceSubstringInFile.py android_arm64-v8a.sh /home/dir/Android/Sdk/ndk-build /home/dir/Android/Sdk/ndkr11c
# Requirements: Python3
# Source: https://stackoverflow.com/a/20593644

import fileinput
import sys

argvLen = len(sys.argv)

text_to_search = sys.argv[argvLen - 2]
replacement_text = sys.argv[argvLen - 1]

for filename in sys.argv[1:argvLen - 2]:
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')
