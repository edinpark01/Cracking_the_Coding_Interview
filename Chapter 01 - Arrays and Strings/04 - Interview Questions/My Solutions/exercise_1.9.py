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
        return True if w2 in (w1 + w1) else False
    else:
        print 'Length mismatch OR string input is empty'
        return False

""" Test Cases """
original_strings = ['waterbottle', 'ABCD', 'ABCD', 'ABCD', ""]
rotated_strings = ['erbottlewat', 'BCDA', 'ACDB', 'ABCDE', ""]


for s1, s2 in zip(original_strings, rotated_strings):
    print(isSubstring(s1, s2))


"""
EXPLANATION:
If we imagine that s2 is a rotation of s1, then we can ask what the rotation point is. 

FOR EXAMPLE, if you rotate WATERBOTTLE after WAT, you get ERBOTTLEWAT. 

In a rotation, we cut s1 into two parts, x and y and rearrange them to get s2.

s1 = xy = [wat][erbottle]

x = wat
y = erbottle

s2 = yx = [erbottle][wat]

So, we need to check if there's a way to split s1 into x and y such that xy = s1 and yx = s2.
Regardless of where the division between x and y is, we can see that yx will always be a substring of xyxy. 
That is, s2 will always be a substring of s1s1.

"""