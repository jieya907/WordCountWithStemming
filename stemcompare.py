from collections import defaultdict
import nltk
import argparse
from nltk import stem
from nltk import word_tokenize
import pprint

lc = stem.lancaster.LancasterStemmer()

parser = argparse.ArgumentParser(description = 'Process a text file.')

parser.add_argument('filename', type=str, help='pathname to that file')

args = parser.parse_args()

print args

filename = args.filename
pp = open(filename)

text = pp.read()

tokens = word_tokenize(text)

lctk = [lc.stem(i) for i in tokens]

lcct = defaultdict(int)

for j in lctk:
    lcct[j] += 1

pprint.pprint(dict(lcct))
