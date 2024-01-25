
# ----- VISUALIZATION -----
# * * * * *                         1*2 - 1, 1 | 0, 4 --> #height-i | 0 spaces on the left, 4 spaces on the right
# * * * *                           2*2 - 1, 3 | 0, 3 --> #height-i | 0 spaces on the left, 3 spaces on the right
# * * *                             3*2 - 1, 5 | 0, 2 --> #height-i | 0 spaces on the left, 2 spaces on the right
# * *                               4*2 - 1, 7 | 0, 1 --> #height-i | 0 spaces on the left, 1 spaces on the right
# *                                 5*2 - 1, 9 | 0, 0 --> #height-i | 0 spaces on the left, 0 spaces on the right

# n or height = 5
# number of index = prev index/variable + 1 


# ----- FUNCTIONS -----

# ----- PSEUDO CODE -----
# - ACTUAL CODE
# - 

def downward_half_pyramid(height):
    for i in range(height, 0, -1):
        stars = '* ' * (i - 1)
        print(stars)

# Calling the function with 5 rows
downward_half_pyramid(6)
