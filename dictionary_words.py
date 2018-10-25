import sys
import random

# Open the file
f = open('/usr/share/dict/words', 'r')
# Put the lines into an array
words = f.readlines()

# Grab the number of words to be in the sentence from argument
numWords = sys.argv[1]

gen_string = []
for i in range(int(numWords)):
    index = random.randint(0, len(words) - 1)
    gen_string.append(words[index].rstrip())

print(' '.join(gen_string) + '.')
f.close()
