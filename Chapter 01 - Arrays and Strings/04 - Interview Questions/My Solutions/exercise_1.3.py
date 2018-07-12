"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
        space at the end to hold the additional characters, and that you are given the 'true' length of the string.
        (NOTE: if implementing in Java, please use a character array so that you can perform this operation in place)
"""

string = '[Mr    John    Smith     ]'

def getNext(str, i):
    n = len(str)
    if i < n:
        return str[i]
    else:
        return None


def URLfy(str):
    i = 0
    c = getNext(str, i)
    temp = ''

    while c != None:
        if not c.isspace():
            temp += c
            i += 1
            c = getNext(str, i)
        else:
            temp += '%20'

            while c.isspace():
                i += 1
                c = getNext(str, i)


    if temp[-4] == '%':
        return temp[0:-4]
    else:
        return temp


print('Input: ' + string)
print('Output: ' + URLfy(string))