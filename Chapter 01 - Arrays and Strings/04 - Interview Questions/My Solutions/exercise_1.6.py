"""
@Student    Braulio Tonaco
@Date       07/14/18

1.6 String Compression:

Implement a method to perform basic string compression using the counts of repeated characters. For example,
the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only uppercase
and lowercase letters (a - z)
"""

"""
NOTES:
1 - If the 'compressed' string is same length as original, RETURN original
2 - ASSUMPTION: input consists of only UPPERCASE and LOWERCASE letters (a - z)
3 - Compressed string consists of a count of consectutive character
    3.1 - If character repeats at diferent locations, its count would not affect previous counts 
"""


def string_compress(s):
    # STEP 0: Initialize compressed string variable
    compresed_string = ''
    compressed = False
    compressing = False
    counter = 0

    # STEP 1: Traverse string
    i = 0
    while i < len(s):
        # STEP 2: retrieve current character and the one next to it
        current_chr = s[i]
        next_chr = s[i + 1] if i + 1 < len(s) else 'reached end'

        # STEP 3: if current IS EQUAL to next character
        if current_chr == next_chr:
            # STEP 3.1: compressing string - set compressing bool to True
            compressing = True

            # STEP 3.2: increment counter by 1 AND continue loop - INCREMENT iterator by 1
            counter += 1
            i += 1
            continue

        # STEP 4: Otherwise - END of string of next character is different than current character
        else:
            # STEP 4.1: If current character was being compressed
            if compressing:
                # STEP 4.1.1: Accumulate compressed string w/ current character and its count + 1
                compresed_string += current_chr + str(counter + 1)

                # STEP 4.1.2: Reset tracking variables
                compressing = False
                counter = 0

                # STEP 4.1.3 string is being compressed, SET compressed bool to true
                compressed = True

            # STEP 4.2: Otherwise, current character count is one
            else:
                # STEP 4.2.1: Accumulate compressed string w/ current character and 1
                compresed_string += current_chr + '1'

        # STEP 5: add 1 to iterator
        i += 1



    # STEP 5: if string go compressed, return its compressed version
    if compressed:
        return compresed_string
    else:
        # STEP 6: Otherwise, return original string
        return s


# TEST cases
test_cases = ['aabcccccaaa', 'abc', 'aabbccaabbccceegGGeFFFFFyyyAAAaa']
correct_out = ['a2b1c5a3', 'abc', 'a2b2c2a2b2c3e2g1G2e1F5y3A3a2']

# Testing
i = 0
for case in test_cases:
    output = string_compress(case)
    expected_output = correct_out[i]
    result = 'True' if output == expected_output else 'False""'

    print('input:\t\t' + case)
    print('output:\t\t' + output)
    print('expected:\t' + expected_output)
    print('CORRECT =>\t' + result + '\n')

    i += 1
