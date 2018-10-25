import sys
import random


def rearrange(args):
    random.shuffle(args)
    return args


if __name__ == '__main__':
    arguments = sys.argv[1:];
    print(' '.join(rearrange(arguments)))
