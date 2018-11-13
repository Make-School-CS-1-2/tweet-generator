from .dictogram import Dictogram
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
            for curr in word_list:
                self.add_count(prev, curr)
                prev = curr
            self.add_word(prev)

    def add_word(self, word, following_word = ""):
        """Increase frequency count of given word and add a new pair if given"""
        if word in self:
            self[word].addCount(following_word)
        else:
            self[word] = 1
            self.types += 1
        self.tokens += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self:
            return self[word].tokens
        return 0
