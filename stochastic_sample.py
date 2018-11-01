import dict_histogram
import random


def get_random_word(histogram):
    return list(histogram.keys())[random.randint(0, len(histogram) - 1)]


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1], mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()

    histogram = dict_histogram.histogram(text)

