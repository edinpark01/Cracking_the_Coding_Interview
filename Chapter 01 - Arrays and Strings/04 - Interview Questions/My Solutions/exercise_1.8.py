"""
@ Student    Braulio Tonaco
@ Date       07/14/18

1.8 Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

"""
from random import randint

# STEP 1: Generate NxM matrix with random numbers from 0 to 10
N = 5
M = 5

matrix = []
for row in range(N):
    matrix.append([])
    for col in range(M):
        random_number = randint(0, 10)
        matrix[row].append(random_number)


# STEP 2: Check if matrix is correctly setup. If so print it
print('Matrix {}x{} constructure'.format(N, M))
for row in matrix:
    print row

# STEP 3: Generate an array of size M filled with 0s
zero_row = [0 for x in range(M)]

zero_col_idx = []
found_zero = False

# STEP 4: Traverse matrix looking for zero elements
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 0:       # found a 0
            found_zero = True       # set found_zero bool to True
            zero_col_idx.append(c)  # save column to be zeroed later

    if found_zero:
        matrix[r] = zero_row        # replace row w/ a zero row if it contained a 0
        found_zero = False          # resets found_zero bool

# STEP 5: Set columns to 0
for row in matrix:
    for col in zero_col_idx:
        row[col] = 0

print

# STEP 6: Print out result matrix
for row in matrix:
    print(row)

