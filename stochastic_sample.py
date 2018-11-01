import dict_histogram
import random

beginner_text = "one fish two fish red fish blue fish"


def get_random_word(histogram):
    return list(histogram.keys())[random.randint(0, len(histogram) - 1)]


def weighted_random_word(histogram):
    word_list = []
    for key, value in histogram.items():
        for _ in range(value):
            word_list.append(key)
    return word_list[random.randint(0, len(word_list) - 1)]


def check_randomness(histogram):
    words = ""
    for _ in range(1000):
        words += weighted_random_word(histogram) + " "
    return dict_histogram.histogram(words)


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1], mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()

    histogram = dict_histogram.histogram(text)

    print(weighted_random_word(histogram))
