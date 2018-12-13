from source.markov_chain import MarkovChain
import random

beginner_text = "one fish two fish red fish blue fish"


def get_random_word(chain):
    return list(chain[random.randint(0, len(chain) - 1)])


def weighted_random_word(chain):
    word_list = []
    for key, value in chain.items():
        for _ in range(value.tokens):
            word_list.append(key)
    return word_list[random.randint(0, len(word_list) - 1)]


def new_weighted_random_histogram(chain, chain_sum):
    count = random.randint(0, chain_sum) 
    for key, value in chain.items():
        count -= value.tokens
        if count <= 0:
            return key


def new_weighted_random_type(histogram):
    count = random.randint(0, histogram.tokens)
    for key, value in histogram.items():
        count -= value
        if count <= 0:
            return key


def check_randomness(chain):
    words = []
    for _ in range(1000):
        words.append(weighted_random_word(chain))
    return MarkovChain(words)


def check_new_randomness(chain, chain_sum):
    words = []
    for _ in range(1000):
        words.append(new_weighted_random_histogram(chain, chain_sum))
    return MarkovChain(words)


def get_chain_sum(chain):
    chain_sum = 0;
    for value in chain.values():
        chain_sum += value.tokens
    return chain_sum;


def make_sentence(chain, number_of_words = 20):
    sentence = []
    first_type = new_weighted_random_histogram(chain, get_chain_sum(chain))
    sentence.extend(first_type)
    for _ in range(20):
        first_word = sentence[len(sentence) - 2]
        second_word = sentence[len(sentence) - 1]
        if (first_word, second_word) in chain.keys():
            add_type = new_weighted_random_type(chain[first_word, second_word])
            sentence.append(add_type)
        else:
            break
    return sentence





if __name__ == '__main__':
    import sys
    f = open(sys.argv[1], mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n'))
    text = text.split(' ')

    chain = MarkovChain(text)

    # print(new_weighted_random_histogram(chain, chain_sum))
    # print(check_new_randomness(chain, chain_sum))
    print(' '.join(make_sentence(chain)))
