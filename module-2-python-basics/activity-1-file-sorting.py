"""
Module 2 — Activity: File Sorting with os and shutil
Student: Navarro, Josell Marion C.
Date: September 30, 2026

============================================
WHAT DID YOU BUILD? 
============================================
Though I didn't finish this activity yet as far as I can remember old sorting activity
where I try to built an automated file organizer script that cleans up 
an unorganized "Downloads" or "Target" folder
by sorting files into categorized subfolders based on their file extensions.


============================================
KEY VOCABULARY
============================================
- os module: It is a built-in Python library used to interact with the operating system.
- shutil module: It is a built-in Python module that provides high-level file operations,
 such as copying, moving, and archiving files or entire folder trees.
- file path: This is the unique text string that specifies the location of a file 
    or directory within a computer's file system
- directory: It is a folder used to store and organize files 
    and other subdirectories on a storage drive.
- os.listdir(path): It is where we returns a list containing the names 
    of all files and folders located inside the given path.

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

dire = input("Enter a Folder Path: ")

if os.path.exists(dire):
    files = os.listdir(dire)
    img = 0
    vid = 0
    doc = 0
    oth = 0

else:
    print("Unknown Directory!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
When I research about this topic, I think moving the folder into themselves and forgetting
to check `os.path.isfile(item_path)` causes `os.listdir()` to pick up the newly created
category folders themselves, attempting to move folders inside folders repeatedly.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
