beginner_text = "one fish two fish red fish blue fish"


def histogram(text):
    import string
    table = str.maketrans({key: None for key in string.punctuation})
    words = text.translate(table).split()
    histogram = {}
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    return 0


if __name__ == '__main__':
    f = open('./don-quixote.txt', mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()

    histogram = histogram(text)

    search_word = "don"

    print("histogram:", histogram)
    print("number of unique words:", unique_words(histogram))
    print("frequency of the word \"%r\":" % search_word, frequency(search_word, histogram))
