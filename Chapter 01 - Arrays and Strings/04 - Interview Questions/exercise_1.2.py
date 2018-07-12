"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
"""

original_str_01 = 'abc'
shuffled_str_01 = 'bac'

original_str_02 = 'abcdefg'
shuffled_str_02 = 'abcdeeg'

def checkPermutation(str1, str2):
    lst_01 = list(str1)
    lst_02 = list(str2)

    sorted_01 = ''.join(sorted(lst_01))
    sorted_02 = ''.join(sorted(lst_02))

    if sorted_01 == sorted_02:
        return True
    else:
        return False


print checkPermutation(original_str_01, shuffled_str_01)

print checkPermutation(original_str_02, shuffled_str_02)
