"""
@Student    Braulio Tonaco
@Date       07/12/18

1.4 Palindrome Permutation:

Given a string, write a function to check if it is a permutation of a palindrome.

A PALINDROME is a word or phrase that is the same forwards and backwards.
A PERMUTATION is a rearrangement of letters.
The PALINDROME does not need to be limited to just dictionary words

EXAMPLE:
Input   ->  tact coa
Output  ->  True (permutations: ['taco cat', 'atco cta', etc]

HINT: You dont have to AND should not have to - generate all permutation, it would be very inefficient
"""

def check(s):
    tracker = {}
    str_len = 0
    for chr in s:
        if not chr.isalpha():
            continue
        if chr not in tracker:
            tracker[chr] = 1
            str_len += 1
        else:
            tracker[chr] += 1
            str_len += 1

    even = False

    print('Characters Count...')

    if str_len % 2 == 0:
        even = True

    for k, v in tracker.items():
        print(k + " -> " + str(v))

    if even:  # EVEN strings that are palindromes - each character count must be even
        print('\nThis string is EVEN')

        for v in tracker.values():
            if v % 2 != 0:
                return False
    else:  # ODD strings that are palindromes - all characters but one (which its count must be 1) must be even
        print('\nThis string is ODD')
        odd_counter = 0
        for v in tracker.values():
            if odd_counter > 1:
                return False
            if v % 2 != 0:
                odd_counter += 1

    return True

string = 'tact coa'

print(check(string))

"""
EXPLANATION

This is a question where it helps to figure out what it mean for a string to be a permutation of a palindrome. 
This is like asking what the 'defining features' of such a string would be. 

A palindrome is a string that is the same forwards and backwards. Therefore, to decide if a string is a 
permutation of a palindrome, we need to know if it can be written such that it is the same forwards and backwards

What does it take to be able to write a set of characters the same way forwards and backwards?
We need to have an even number of almost all characters, so that half can be on one side and half can be on the other
side. At most one character (the middle character) can have an odd count. 
"""