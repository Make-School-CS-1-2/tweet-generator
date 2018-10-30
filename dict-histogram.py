beginner_text = "one fish two fish red fish blue fish"


def histogram(text):
    words = text.split()
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
    return histogram[word]


if __name__ == '__main__':
    f = open('./don-quixote.txt', mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()

    histogram = histogram(text)

    print("histogram:", histogram)
    print("number of unique words:", unique_words(histogram))
    print("frequency of the word \"don\":", frequency("don", histogram))
