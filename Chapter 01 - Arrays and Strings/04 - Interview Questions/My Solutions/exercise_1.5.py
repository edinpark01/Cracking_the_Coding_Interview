"""
@Student    Braulio Tonaco
@Date       07/12/18

1.5 One Away:
There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE:
    pale,   ple     ->  True
    pales,  pale    ->  True
    pale,   bale    ->  True
    pale,   bake    ->  False
"""

str_list = [
    ('pale',     'ple'),
    ('pales',    'pale'),
    ('pale',     'bale'),
    ('pale',     'bake'),
    ('pal',      'pale'),
    ('edu',      'edu'),
    ('edu',      'eduardo')
]


def one_replace_away(str1, str2):
    print(str1 + " -> " + str2)
    bad_chr_found = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            bad_chr_found += 1
        if bad_chr_found > 1:  # If more than 1 chr needs to be replaced, MORE than 1 edit required
            return False

    return True


def one_insert_away(str1, str2):
    print(str1 + " -> " + str2)

    idx1 = 0
    idx2 = 0

    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] != str2[idx2]:
            if idx1 != idx2:
                return False
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1

    return True

def one_away(lst):
    for s1, s2 in lst:

        if s1 == s2:
            print 'ZERO edit away, strings are equal'
        elif len(s1) == len(s2):
            print one_replace_away(s1, s2)
        elif abs(len(s1) - len(s2)) == 1:
            result = one_insert_away(s2, s1) if len(s1) > len(s2) else one_insert_away(s1, s2)                             # EDIT -> INSERT
            print result
        else:
            print('MORE than 1 edit required: False')

        print('\n')


one_away(str_list)


"""
EXPLANATION

    This is one of those problems where it's helpful to think about the 'meaning' of each of these operations. 
What does it mean for two strings to be one insertion, replacement, or removal away from each other?
    REPLACEMENT: Consider two strings, that are one replacement away. Yes, that does mean that you could replace a 
                 character in bale to make a pale. But more precisely, it means that they are different only in 
                 one place
    INSERTION:   The strings apple and aple are one insetion away. This means that if you compared the strings, 
                 they would be identical -except for a shift at some point in the string.
    REMOVAL      The strings apple and aple are also one removal away, since removal is just the inverse of 
                 insetion
"""



