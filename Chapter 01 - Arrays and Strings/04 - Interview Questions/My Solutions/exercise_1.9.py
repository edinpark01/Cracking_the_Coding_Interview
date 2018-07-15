"""
@ Student    Braulio Tonaco
@ Date       07/14/18

1.9 String Rotation:
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring

EXAMPLE:
WATERBOTTLE is a rotation of ERBOTTLEWAT

"""

def isSubstring(w1, w2):
    if len(w1) == len(w2) and len(w1) > 0:
        return True if w1 in (w2 + w2) else False
    else:
        print 'Length mismatch OR string input is empty'
        return False

""" Test Cases """
original_strings = ['waterbottle', 'ABCD', 'ABCD', 'ABCD', ""]
rotated_strings = ['erbottlewat', 'BCDA', 'ACDB', 'ABCDE', ""]


for s1, s2 in zip(original_strings, rotated_strings):
    print 's1: ' + s1
    print 's2: ' + s2

    print(isSubstring(s1, s2))
