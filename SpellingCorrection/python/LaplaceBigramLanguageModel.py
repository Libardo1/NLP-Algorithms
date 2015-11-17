import math, collections

class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.LaplaceUnigramCounts = collections.defaultdict(lambda: 1)
    self.LaplaceBigramCounts = collections.defaultdict(lambda: 1)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
        prev_word = "<s>"
        for datum in sentence.data[1:]:  
            token = datum.word
            bigram = (prev_word, token)
            self.LaplaceUnigramCounts[token] += 1
            self.LaplaceBigramCounts[bigram] += 1
            self.total += 1
            prev_word = token

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    V = len(self.LaplaceUnigramCounts) 

    prev_word = "<s>"
    for token in sentence[1:]:
        bigram = (prev_word, token)
        score += math.log(self.LaplaceBigramCounts[bigram])
        score -= math.log(self.LaplaceUnigramCounts[prev_word] + V)
        prev_word = token
    return score
