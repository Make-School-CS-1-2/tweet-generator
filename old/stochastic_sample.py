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


def new_weighted_random_word(chain, chain_sum):
    count = random.randint(0, chain_sum)  # change the sum to a arg, this is reducing efficiency
    for key, value in chain.items():
        count -= value.tokens
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
        words.append(new_weighted_random_word(chain, chain_sum))
    return MarkovChain(words)


def get_chain_sum(chain):
    chain_sum = 0;
    for value in chain.values():
        chain_sum += value.tokens
    return chain_sum;


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1], mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()
    text = text.split(' ')

    chain = MarkovChain(text)

    chain_sum = get_chain_sum(chain)

    print(new_weighted_random_word(chain, chain_sum))
    print(check_new_randomness(chain, chain_sum))
