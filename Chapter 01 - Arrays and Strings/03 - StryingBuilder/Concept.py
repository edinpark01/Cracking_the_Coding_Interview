"""
Imagine you are concatenating a list of strings, as shown below. What would the running time of this code be?
For simplicity, assume that the strings are all the same length (call this x) and that there are n string.
"""

def joinWords(words):
    sentence = ''

    for word in words:
        # len (word) = x
        sentence = sentence + word

    return sentence

"""
1st iteration: 0  + x = x  => a new string of size x is created and then each char is copied over
2nd iteration: x  + x = 2x => a new string of size 2x is created and then each char is copied over
3rd iteration: 2x + x = 3x => a new string of size 3x is created and then each char is copied over
4th iteration: 3x + x = 4x => a new string of size 4x is created and then each char is copied over
5th iteration: 5x + x = 5x => a new string of size 5x is created and then each char is copied over
.
.
.
nth iteration: nx + x = x(n + 1)


O(x + 2x + 3x + 4x + 5x + ... + nx) = xn(n + 1) / 2 = O(n^2) 
"""
