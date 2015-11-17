import math, collections

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.LaplaceUnigramCounts = collections.defaultdict(lambda: 1)
    self.LaplaceBigramCounts = collections.defaultdict(lambda: 0)
    self.LaplaceTrigramCounts = collections.defaultdict(lambda: 0)
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

            if prev_word != "<s>":
                trigram = (preprev_word, prev_word, token) 
                self.LaplaceTrigramCounts[trigram] += 1

            self.total += 1
            preprev_word = prev_word
            prev_word = token 

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    V = len(self.LaplaceUnigramCounts) 

    preprev_word = "<s>"
    prev_word = sentence[1]
    for token in sentence[2:]:
        bigram = (prev_word, token)
        trigram = (preprev_word, prev_word, token) 
        if trigram in self.LaplaceTrigramCounts:
            score += math.log(self.LaplaceTrigramCounts[trigram])
            score -= math.log(self.LaplaceBigramCounts[bigram])

        elif bigram in self.LaplaceBigramCounts:
            score += math.log(self.LaplaceBigramCounts[bigram])
            score += math.log(0.4)
            score -= math.log(self.LaplaceUnigramCounts[prev_word])

        else:
            score += math.log(self.LaplaceUnigramCounts[token])
            score -= math.log(self.total + V)
        preprev_word = prev_word
        prev_word = token
    return score
