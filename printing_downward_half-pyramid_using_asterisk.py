
# ----- VISUALIZATION -----
# * * * * *                         5*1 - 0, 5 | 0, 4 --> #height-i | 0 spaces on the left, 0 spaces on the right
# * * * *                           4*1 - 0, 4 | 0, 3 --> #height-i | 0 spaces on the left, 1 spaces on the right
# * * *                             3*1 - 0, 3 | 0, 2 --> #height-i | 0 spaces on the left, 2 spaces on the right
# * *                               2*1 - 0, 2 | 0, 1 --> #height-i | 0 spaces on the left, 3 spaces on the right
# *                                 1*1 - 0, 1 | 0, 0 --> #height-i | 0 spaces on the left, 4 spaces on the right


# ----- FUNCTIONS -----
# - def function for downward half-pyramid
def downward_half_pyramid(height):
    for i in range(height, 0, -1):
        print(("*" + " ") * ((i*1)-0), end= " ")
        print(" " * (height - i))

# >>>>>>>>>> PSEUDO CODE <<<<<<<<<<
# ----- ACTUAL CODES -----
# - Caller of the def function/s
downward_half_pyramid(5)