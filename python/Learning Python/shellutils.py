#
# Example file for working with filesystem shell methods
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
# Make a duplicate of an existing file
    if path.exists("textfile.txt.bak"):

# Get the path to the file in the current directory
        src = path.realpath("textfile.txt")

# Let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"
    # shutil.copy(src, dst)

# Rename the original file
    # os.rename("textfile.txt", "newfile.txt")

# Now put things intp a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

# More fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()