def levenshtein(s1, s2, cost_sub):
    """Takes 2 words and a cost of substitution, returns Levenshtein distance.
    
    >>>levenshtein('foo', 'poo', cost_sub=2)
    2
    
    >>>levenshtein('intention', 'execution', cost_sub=2)
    8
    
    """
    if len(s1) < len(s2): # If one word is shorter than the other then change the order (bookkeeping to be consistent)
        return levenshtein(s2, s1, cost_sub)
 
    if len(s2) == 0: # Make are getting a real word, 
        # if we are not getting a real word the cost is simply dropping all the letters in one of the words i.e. the length
        return len(s1)
 
    previous_row = range(len(s2) + 1) # Creating an array of length of the second word+1
   
    for i, c1 in enumerate(s1): # Interate through the first word 
        current_row = [i + 1]
        for j, c2 in enumerate(s2): # Interate through the second word
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1 
            substitutions = previous_row[j] + ((c1 != c2) * cost_sub)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]