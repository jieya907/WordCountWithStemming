from collections import defautldict
import nltk
import argparse
from nltk import stem
from nltk import word_tokenize

lc = stem.lancaster.LancasterStemmer()

parser = argparse.ArgumentParser(description = 'Process a text file.')

parser.add_argument('filename', type=str, help='pathname to that file')

args = parser.parse_args()

print args

pp = open(filename)

text = pp.read()

tokens = word_tokenize(text)

lctk = [lc.stem(i) for i in tokens]

lcct = defaultdict(int)

for j in lctk:
    lcct[j] += 1

pprint.pprint(lcct)
