from dictogram import Dictogram, print_histogram
class MarkovChain(dict):
    """MarkovChain is a dictionary which holds Dictograms
     This shows the amount of times a word occurs after the chosen word"""
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(MarkovChain, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        # Done: Initialize from parameter
        if word_list is not None:
            prev = word_list[0]
            for curr in word_list[1:]:
                self.add_word(prev, curr)
                prev = curr
            self.add_word(prev)

    def add_word(self, word, next_word = None):
        """Increase frequency count of given word and add a new pair if given"""
        if word not in self:
            self.types += 1
            if next_word:
                self[word] = Dictogram([next_word])
        elif next_word:
            self[word].add_count(next_word)
        self.tokens += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self:
            return self[word].tokens
        return 0


def print_markov_chain(word_list):
    print('word list: {}'.format(word_list))
    # Create a MarkovChain and display its contents
    markov_chain = MarkovChain(word_list)
    print('MarkovChain: {}'.format(markov_chain))
    print('{} tokens, {} types'.format(markov_chain.tokens, markov_chain.types))
    for word in word_list[-2:]:
        freq = markov_chain.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
        print('{!r}  pairs:'.format(word))
        print(markov_chain[word])
    print()


if __name__ == "__main__":
    word_list = list("abracadabra")
    print_markov_chain(word_list)
