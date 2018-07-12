# IS UNIQUE? Implement an algorithm to determine if a string has all unique characters. What if you can't
#            use any additional data structure.

unique_str = 'abcdef'
non_unique_str = 'abcdefgre'

def isUnique(str):
    lst = []

    for i in range(128):
        lst.append(True)

    for c in str:
        ascii = ord(c)

        if lst[ascii] == False:
            return 'Not Unique'

        lst[ascii] = False

    return 'Unique'

print(isUnique(unique_str))
print(isUnique(non_unique_str))