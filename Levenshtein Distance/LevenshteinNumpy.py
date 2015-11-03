import numpy as np

def levenshtein_numpy(s1, s2, cost_sub):
    """Takes 2 words and a cost of substitution, returns Levenshtein distance.
    
    >>>levenshtein('foo', 'poo', cost_sub=2)
    2
    
    >>>levenshtein('intention', 'execution', cost_sub=2)
    8
    
    """
    if len(s1) < len(s2): # If one word is shorter than the other then change the order (bookkeeping to be consistent)
        return levenshtein(s2, s1, cost_sub)
 
    if len(s2) == 0: # Make are getting a real word, 
        # if we are not getting a real word the cost is simply dropping all the letters in one of the words
        return len(s1)
    
    D = np.zeros((len(s1)+1,len(s2)+1))
    D[0] = range(len(s2)+1)
    D[:,0] = range(len(s1)+1)
    
    for i, letter1 in enumerate(s1, start = 1):
        for j, letter2 in enumerate(s2, start = 1):
            D[i,j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1,j-1] + (letter1 != letter2)*cost_sub )
    return D[-1][-1]