#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]

    length = len(arguments)
    if length == 0:
        print('0 arguments.')
    elif length == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(length), end='\n')

    for i, args in enumerate(arguments, start=1):
        print("{:d}: {:s}".format(i, args))
