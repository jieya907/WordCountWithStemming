import operator 
from collections import defaultdict
import nltk
import argparse
from nltk import stem
from nltk import word_tokenize
import pprint
import sys

#This is to get rid of the utf-8 and ascii encoding problem
reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()

CUTOFF = 50

def basecnt(words):
    """
    Give a list of words, count them to a dictionary. Word to word count
    """
    bsct = defaultdict(int)
    for j in words:
        bsct [j] += 1
    sort_cnt = sorted(bsct.items(), key = operator.itemgetter(1))
    sort_cnt.reverse()
    return sort_cnt

def lcstem(words):
    """
    Give a list of words, using the Lancaster stemmer to stem the words
    then output a list of tuples, first item is the word, second is the 
    occurrence of the word 
    """
    lc = stem.lancaster.LancasterStemmer()
    # tokenizing using lancaster stemmer 
    lctk = [lc.stem(i) for i in words]
    return basecnt(lctk)

def sbstem(words):
    """
    Give a list of words, using the snowball stemmer to stem the words
    then output a list of tuples, first item is the word, second is the 
    occurrence of the word 
    """
    lc = stem.snowball.SnowballStemmer("english")
    # tokenizing using lancaster stemmer 
    lctk = [lc.stem(i) for i in words]
    return basecnt(lctk)



parser = argparse.ArgumentParser(description = 'Process a text file.')

parser.add_argument('filename', type=str, help='pathname to that file')

args = parser.parse_args()

print args

filename = args.filename
pp = open(filename)

# string of the text 
text = pp.read()

# the list of words 
tokens = word_tokenize(text)

allwd = basecnt(tokens)
print "all words in the text, without stemming"
print allwd[:CUTOFF] 
#
print "words in text with snow ball stemming" 
sbwd = sbstem(tokens)
print sbwd[:CUTOFF]

print "words in text with lancasterstemming" 
lcwd = lcstem(tokens)
print lcwd[:CUTOFF]

