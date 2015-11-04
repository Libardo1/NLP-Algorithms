import textwrap

def justification(s, width)
    for text in textwrap.wrap(s, 60):
        sentence = text.split()
        
        num_char = len(reduce(lambda a, b: a+b, sentence))
        space_add = width - num_char
        
        while space_add > 0:    
            for i in range(len(sentence[:-1])):
                if space_add > 0:
                    sentence[i] += " "
                    space_add -= 1
                else:
                    break

        print "".join(sentence)

if __name__ == '__main__':
    s = "Obtain some raw text, in the form of a single, \
    long string. Use Python's textwrap module to break it up into multiple lines. \
    Now write code to add extra spaces between words, in order to justify the output. \
    Each line must have the same width, and spaces must be approximately evenly distributed \
    across each lines. No line can begin or end with a space. Look into Python docs for string formatting."

    justification(s, 60)