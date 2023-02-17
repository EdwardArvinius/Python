#!/usr/bin/python

import os
import shutil
import fileinput
import string

while True:
    print("""
    1. Add line number
    2. Delete line number
    3. Change file name extension
    4. Backup file
    5. Reverse file
    6. Exit/Quit
    """)

    choice = input("What would you like to do? ")

    if choice == "1":
        infile = open('line1.txt', 'r')
        lines = infile.readlines()
        infile.close()
        outtext = ['%d %s' % (i, line) for i, line in enumerate(lines)]
        outfile = open("line1.txt", "w")
        outfile.writelines(str("".join(outtext)))
        outfile.close()

    elif choice == "2":
        for line in fileinput.input("line1.txt", inplace=True):
            print(line.translate(None, string.digits), end='')

    elif choice == "3":
        print("\nOld file name: file.cxx")
        print("\nNew file name: " + os.path.splitext('file.cxx')[0] + '.cpp')

    elif choice == "4":
        file_path = 'line1.txt'
        backup_dir = '.backup'

        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Copy the file to the backup directory
        shutil.copy2(file_path, os.path.join(backup_dir, os.path.basename(file_path) + '.bak'))
        print(f'File {file_path} backed up successfully.')

    elif choice == "5":
        print("\nBefore reverse")
        with open('text1.txt', 'r') as f:
            file_contents = f.read()
            print(file_contents)

        print("\nAfter reverse")
        with open('text1.txt', 'r') as f:
            for line in reversed(f.readlines()):
                print(line.rstrip())

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nNot a valid choice. Try again.")

