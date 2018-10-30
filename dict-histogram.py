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


if __name__ == '__main__':
    f = open('./don-quixote.txt', mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()
    print(histogram(text))
