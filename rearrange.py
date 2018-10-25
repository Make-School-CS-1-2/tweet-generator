import sys
import random

words = sys.argv[1:len(sys.argv)]

random.shuffle(words)

print(' '.join(words))