# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
goal = [3, 3]
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[goal[0]][goal[1]] = 1
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    x, y = goal[0], goal[1]
    g = 0

    opens = [[g,x,y]]

    found = False
    resign = False
    count = 0

    while opens:
    	opens.sort()
    	opens.reverse()
        next = opens.pop()
        x,y,g = next[1],next[2],next[0]
        value[x][y] = g
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                if closed[x2][y2] == 0:
                    if grid[x2][y2] == 1:
                        value[x2][y2] = 99
                    else:
                        g2 = g + cost_step
                        opens.append([g2,x2,y2])
                    closed[x2][y2] = 1
    return value #make sure your function returns a grid of values as demonstrated in the previous video.

def optimum_policy():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[goal[0]][goal[1]] = 1
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x, y = goal[0], goal[1]
    g = 0

    opens = [[g,'*',x,y]]

    found = False
    resign = False
    count = 0

    while opens:
        opens.sort()
        opens.reverse()
        next = opens.pop()
        x,y,g,s = next[2],next[3],next[0],next[1]
        policy[x][y] = s
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                if closed[x2][y2] == 0:
                    if grid[x2][y2] == 1:
                        policy[x2][y2] = ' '
                    else:
                        g2 = g + cost_step
                        s = delta_name[(i+2) % 4]
                        opens.append([g2,s,x2,y2])
                    closed[x2][y2] = 1

    return policy

result = compute_value()
for row in result:
	print row

result = optimum_policy()
for row in result:
    print row