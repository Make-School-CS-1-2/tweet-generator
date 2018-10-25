import random
import sys


def random_words(num_words):
    # Open the file
    f = open('/usr/share/dict/words', 'r')
    # Put the lines into an array
    words = f.readlines()

    gen_string = []
    for i in range(int(num_words)):
        gen_string.append(words[random.randint(0, len(words) - 1)].rstrip())

    return gen_string
    f.close()


if __name__ == '__main__':
    num_words = int(sys.argv[1])
    output = random_words(num_words=num_words)
    print(' '.join(output) + '.')


