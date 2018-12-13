import fileinput
import re
import sys


def main():
    print(sys.argv)
    pattern, filename = sys.argv[1:] # get pattern, filename from command-line
    matched = re.compile(pattern).search
    with fileinput.FileInput(filename, inplace=1, backup='.bak') as file:
        for line in file:
            if not matched(line): # save lines that do not match
                print(line, end='') # this goes to filename due to inplace=1


if __name__ == '__main__':
    main()