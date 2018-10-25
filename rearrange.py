import sys
import random


def rearrange(args):
    random.shuffle(args)
    print(' '.join(args))


if __name__ == '__main__':
    arguments = sys.argv[1:];
    rearrange(arguments)
