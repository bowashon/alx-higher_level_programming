#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if i == ord(c):
            return True
    else:
        return False


def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) if not islower(c) else ord(c) - 32), end='')
    else:
        print()
