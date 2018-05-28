#!/usr/bin/env python
#encoding: utf-8
import os;
import webbrowser;
import shutil;

def main():
    os.chdir("C:");
    command = input("Enter a command, or HELP to see a list of commands. >> ");
    commands(command);

def commands(cmd):
    if cmd == "HELP" or cmd == "help":
        print("""HELP: Display all available commands.
CD(dir): Change current directory.
LS: List all items within current directory.
PWD: Display current directory.
OPEN(filename): Opens selected file.
TOUCH(filename): Create a file with given name.
MKDIR(directory name): Create a directory with given name.
CP(filename): Duplicate the selected file.
RM(filename): Delete the selected file. WARNING: THIS ACTION IS IRREVERSIBLE!
RMDIR(directory name): Delete the selected directory (must be empty).
RM-R(directory name): Delete the selected directory and all it's contents.""");
    if cmd == "CD" or cmd == "cd":
        dir = input("Directory path >> ");
        os.chdir(str(dir));

    if cmd == "LS" or cmd == "ls":
        print(os.listdir());

    if cmd == "PWD" or cmd == "pwd":
        print(os.getcwd());

    if cmd == "OPEN" or cmd == "open":
        file = input("Filename >> ");
        webbrowser.open(file);

    if cmd == "TOUCH" or cmd == "touch":
        file = input("Filename >> ");
        webbrowser.open(file, w+);

    if cmd == "MKDIR" or cmd == "mkdir":
        dir = input("Directory name >> ");
        os.mkdir(dir);

    if cmd == "CP" or cmd == "cp":
        file = input("Filename >> ");
        shutil.copyfile(file, file + "(1)");

    if cmd == "RM" or cmd == "rm":
        file = input("Filename >> ");
        os.remove(file);

    if cmd == "RMDIR" or cmd == "rmdir":
        dir = input("Directory name >> ");
        os.rmdir(dir);

    if cmd == "RM-R" or cmd == "rm-r":
        dir = input("Directory name >> ");
        shutil.rmtree(dir);

if __name__ == '__main__':
    while True:
        main();
