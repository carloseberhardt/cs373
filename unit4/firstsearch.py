# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    initial = [0] + init
    visited = []
    expanded = []
    result = walk(initial, visited, expanded)
    return result

def walk(start, visited, expanded):
    if start[1:] == goal:
        return start
    else:
        visited.append(start[1:])
        expanded = expand(expanded, visited, start)
        if len(expanded) == 0:
            return "fail"
        start, expanded = select(expanded)
        return walk(start, visited, expanded)


def expand(expanded, visited, spot):
    for mv in delta:
        cell = [spot[0] + cost] + map(lambda x,y: x+y, spot[1:], mv)
        inbounds = (-1 < cell[1] < len(grid)) and (-1 < cell[2] < len(grid[0]))
        newspot = cell[1:] not in visited 
        newspot = newspot and cell[1:] not in [x[1:] for x in expanded]
        if inbounds and newspot:
            openspot = grid[cell[1]][cell[2]] != 1
            if openspot:
                expanded.append(cell)
    return expanded


def select(expanded):
    expanded.sort(reverse=True)
    newspot = expanded.pop()
    return newspot, expanded

print search()
