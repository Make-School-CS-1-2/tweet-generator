import sys
import random


def rearrange(args):
    output_list = args[:]
    random.shuffle(output_list)
    return output_list


if __name__ == '__main__':
    arguments = sys.argv[1:];
    print(' '.join(rearrange(arguments)))
