# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():

    value = [
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    ]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if [x, y] == goal:
                    for d in range(len(value)):
                        if value[d][x][y] > 0:
                            value[d][x][y] = 0
                            policy2D[x][y] = '*'
                            change = True
                elif grid[x][y] == 0:
                    for a in range(len(forward)):
                        x2 = x + forward[a][0]
                        y2 = y + forward[a][1]
                        if (x2 >= 0 and x2 < len(grid) 
                                    and y2 >= 0 and y2 < len(grid[0]) 
                                    and grid[x2][y2] == 0):
                            #figure out direction here
                            heading = (a+2)%4
                            print [x,y], [x2,y2], forward[heading]
                            v2 = value[0][x2][y2] + cost[1]
                            if v2 < value[0][x][y]:
                                print a, [x,y]
                                value[0][x][y] = v2
                                policy2D[x][y] = '?'
                                change = True
    return policy2D, value # Make sure your function returns the expected grid.

result,value = optimum_policy2D()
for row in result:
    print row
for row in value:
    print " "
    for anotherrow in row:
        print anotherrow

def optimum_policy():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost_step

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]
 
    return policy # Make sure your function returns the expected grid.