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
            prev1 = word_list[0]
            prev2 = word_list[1]
            for curr in word_list[2:]:
                self.add_word((prev1, prev2), curr)
                prev1 = prev2
                prev2 = curr
            self.add_word((prev1, prev2))

    def add_word(self, pair, next_pair = None):
        """Increase frequency count of given word and add a new pair if given"""
        if pair not in self:
            self.types += 1
            if next_pair:
                self[pair] = Dictogram([next_pair])
        elif next_pair:
            self[pair].add_count(next_pair)
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
    for index in range(len(word_list[-3:])):
        freq = markov_chain.frequency((word_list[index], word_list[index + 1]))
        print('{!r} occurs {} times'.format((word_list[index], word_list[index + 1]), freq))
        print('{!r}  pairs:'.format((word_list[index], word_list[index + 1])))
        print(markov_chain[(word_list[index], word_list[index + 1])])
    print()


if __name__ == "__main__":
    word_list = list("abracadabra")
    print_markov_chain(word_list)
