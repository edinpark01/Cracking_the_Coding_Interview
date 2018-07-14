"""
@ Student    Braulio Tonaco
@ Date       07/14/18

1.7 Rotate Matrix:
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
the image by 90 degrees. Can you do this in place?

"""

"""

NOTES:

top_left        ->  top_right
top_right       ->  bottom_right
bottom_right    ->  bottom_left
bottom_left     ->  top_left

ORIGINAL 5x5 matrix 
[ (0,0), (0,1), (0,2), (0,3), (0,4) ]
[ (1,0), (1,1), (1,2), (1,3), (1,4) ]
[ (2,0), (2,1), (2,2), (2,3), (2,4) ]
[ (3,0), (3,1), (3,2), (3,3), (3,4) ]
[ (4,0), (4,1), (4,2), (4,3), (4,4) ]

ROT 90 degrees 5x5 matrix 
[ (4,0), (3,0), (2,0), (1,0), (0,0) ]
[ (4,1), (3,1), (2,1), (1,1), (0,1) ]
[ (4,2), (3,2), (2,2), (1,2), (0,2) ]
[ (4,3), (3,3), (2,3), (1,3), (0,3) ]
[ (4,4), (3,4), (2,4), (1,4), (0,4) ]
]

"""

def print_matrix(m):
    """ Prints matrix """
    for row in m:
        for cell in row:
            print cell[0],
        print

def initialize_matrix(N):
    """ Constructs and returns NxN matrix """
    temp_matrix = []

    for row in range(N):
        temp_matrix.append([])  # Adds N new row(s)

        for col in range(N):
            element = '|'

            if row == col:
                element = '*'

            temp_matrix[row].append(element)  # Adds N new column(s)

    return temp_matrix


def rotate_matrix(m):
    """ Rotates NxN matrix 90 degrees clockwise """
    N = len(m)
    temp_matrix = initialize_matrix(N)

    col = N - 1

    # Starts at 0x0 -> 0xN then
    #           0x1 -> 1xN
    #           0x2 -> 2xN
    #            .      .
    #            .      .
    #            .      .
    #           0xN -> NxN
    for original_row in m:                              # For each row
        row = 0
        for original_cell in original_row:              # Take original cell

            temp_matrix[row][col] = original_cell
            row += 1

        col -= 1

    return temp_matrix


size = input('Enter Matrix N size: ')

matrix = initialize_matrix(size)

print('Original Matrix')
print_matrix(matrix)

rot_matrix = rotate_matrix(matrix)

print('\nRotated Matrix')
print_matrix(rot_matrix)



