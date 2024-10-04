#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: ngautam11

import subprocess

def free_space():
    # Launch the command to get free disk space and return the result as utf-8
    result = subprocess.run(
        ["df", "-h"], capture_output=True, text=True
    )
    # Find the line that contains the root directory information
    for line in result.stdout.splitlines():
        if line.startswith('/'):
            # Use awk to get the fourth column, which is the free space
            free_space_value = line.split()[3]
            return free_space_value.strip()

if __name__ == '__main__':
    print(free_space())
