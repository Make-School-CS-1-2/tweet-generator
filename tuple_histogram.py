beginner_text = "one fish two fish red fish blue fish"


def histogram(text):
    import string
    table = str.maketrans({key: None for key in string.punctuation})
    words = text.translate(table).split()
    histogram = [(words[0], 0)]
    for word in words:
        found = False
        for i in range(len(histogram)):
            if word in histogram[i][0]:
                old = histogram[i]
                histogram[i] = (word, old[1] + 1)
                break
        if not found:
            histogram.append((word, 1))
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    for i in histogram:
        if word in i[0]:
            return i[1]
    return 0


if __name__ == '__main__':
    f = open('./don-quixote.txt', mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()

    histogram = histogram(text)

    search_word = "fish"

    print("histogram:", histogram)
    print("number of unique words:", unique_words(histogram))
    print("frequency of the word %s:" % search_word, frequency(search_word, histogram))