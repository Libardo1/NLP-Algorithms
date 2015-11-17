from __future__ import (absolute_import, 
                        division,
                        print_function,
                        unicode_literals)


import nltk
import random
from collections import Counter, defaultdict

with open("data/one_fish_by_dr_seuss.txt") as f:
    text = f.read().decode('utf8').replace('\n',  ' ')

tokens = nltk.tokenize.word_tokenize(text.lower())

def unigram(tokens):
    vocab = Counter(tokens)
    V = float(len(vocab))
    return {word: vocab[word] / V for word in vocab}

def bigram(tokens):
    bigram = defaultdict(int)
    bigram_list  = []
    
    prev_word = tokens[0]
    for word in tokens[1:]:
        bigram_list.append((prev_word, word))
        prev_word = word
        
    vocab = Counter(tokens)
    bigram_counts = Counter(bigram_list)
    
    return {key: value / vocab[key[0]] for key, value in bigram_counts.iteritems()}

def smooth_bigram(tokens):
    bigram = defaultdict(int)
    bigram_list  = []
    
    prev_word = tokens[0]
    for word in tokens[1:]:
        bigram_list.append((prev_word, word))
        prev_word = word
        
    vocab = Counter(tokens)
    bigram_counts = Counter(bigram_list)
    V = len(vocab)
    
    return {key: (value + 1) / (vocab[key[0]] + V) for key, value in bigram_counts.iteritems()}


def text_generator(tokens, num_words):
    u  = unigram(tokens)
    b = bigram(tokens)
    
    first_word = random.choice(u.keys())
    text = [first_word]

    for _ in range(num_words):
        keys = [key for key in b if key[0] == first_word]

        first_word = max(keys, key= lambda k: b[k])[1]
        text.append(first_word)

    print(" ".join(text)) 