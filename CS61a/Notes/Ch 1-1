#### Getting started
## example of functions, objects and expressions 

from urllib.request import urlopen

# open url
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

# decode text, split and place all words in a set
words = set(shakespeare.read().decode().split())

# all words that also spell a word in reverse, contained in the set
pairs = {w for w in words if len(w) == 6 and w[::-1] in words}

print (pairs)
