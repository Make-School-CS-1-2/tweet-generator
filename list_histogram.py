beginner_text = "one fish two fish red fish blue fish"


def histogram(text):
    words = text.split()
    histogram = [[words[0], 0]]
    for word in words:
        found = False
        for i in histogram:
            if word in i[0]:
                i[1] += 1
                found = True
        if not found:
            histogram.append([word, 1])
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

    search_word = "don"

    print("histogram:", histogram)
    print("number of unique words:", unique_words(histogram))
    print("frequency of the word \"%r\":" % search_word, frequency(search_word, histogram))
