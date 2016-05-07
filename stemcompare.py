import operator 
from collections import defaultdict
import nltk
import argparse
from nltk import stem
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
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


def pformat(wdlst):
    s = "There are " + str(len(wdlst)) + " unique words in " + filename
    print s
    s1 = "The most frequent " + str(CUTOFF) + " words are "
    print s1
    print wdlst[:CUTOFF]


def process_words(words):
    allwd = basecnt(words)
    print "all words in the text, without stemming"
    pformat(allwd)

    print "words in text with snow ball stemming" 
    sbwd = sbstem(words)
    pformat(sbwd)

    print "words in text with lancasterstemming" 
    lcwd = lcstem(words)
    pformat(lcwd)

def filter_stopwords(words):
    important_words = filter(lambda x: x not in stopwords.words('english'), words)
    return important_words

#Parsing the command line arguments for the filename 
parser = argparse.ArgumentParser(description = 'Process a text file.')
parser.add_argument('filename', type=str, help='pathname to that file')
parser.add_argument('cut_off', type=int, help='cut off value for the list output')
args = parser.parse_args()
print args

filename = args.filename
#open the file 
pp = open(filename)
CUTOFF = args.cut_off
# string of the text 
text = pp.read()
# the list of words 
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)

print "Without filtering out the stop words"
process_words(tokens)

print "With stop words filtering" 

fil_token = filter_stopwords(tokens)
process_words(fil_token)
