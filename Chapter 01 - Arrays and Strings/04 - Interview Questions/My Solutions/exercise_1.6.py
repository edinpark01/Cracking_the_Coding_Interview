"""
@Student    Braulio Tonaco
@Date       07/14/18

1.6 String Compression:

Implement a method to perform basic string compression using the counts of repeated characters. For example,
the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only uppercase
and lowercase letters (a - z)
"""

def string_compress(s):
    #STEP 0: Initialize compressed string & list to assist w/ character counts
    c_s = ''
    lst = []
    compressed = False

    #STEP 1: Traverse string
    for char in s:
        # STEP 2: If character not in list
        if char not in lst:
            # STEP 2.1: Append character to list AND append first count, which is 1
            lst.append(char)
            lst.append(1)

        # STEP 3: If character in list
        else:
            # STEP 3.1: Get its index location and increment its index + 1 by 1
            idx = lst.index(char)
            lst[idx + 1] += 1

            # STEP 3.2: Set compressed to True
            compressed = True

    # STEP 5: Once done compressing string check boolean to make sure that at least one character had multiples
    if not compressed:
        # STEP 5.1: if not character multiples, return original string
        return s
    else:
        # STEP 5.2: Otherwise, iterate over list to return compressed string
        i = 0
        while i < len(lst):
            character = str(lst[i])
            count = str(lst[i + 1])
            c_s += character + count

            i += 2
        return c_s

string = 'aabcccccaaa'
string_2 = 'abc'

compressed_string = string_compress(string_2)

print(compressed_string)