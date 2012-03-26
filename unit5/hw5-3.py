# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother. 
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates. 
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path=[[0, 0], #fix 
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]

# Do not modify fix inside your function
fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

######################## ENTER CODE BELOW HERE #########################
class Point:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    def __add__(self, p):
        return Point(self.x + p[0], self.y + p[1])
    def __sub__(self, p):
        return Point(self.x - p[0], self.y - p[1])
    def __iadd__(self, p):
        self.x += p[0]
        self.y += p[1]
        return self
    def __isub__(self, p):
        self.x -= p[0]
        self.y -= p[0]
        return self
    def __rmul__(self,m):
        return self.__mul__(m)
    def __mul__(self,m):
        m = float(m)
        return Point(self.x * m, self.y * m)
    def __div__(self,d):
        d = float(d)
        return Point(self.x / d, self.y / d)
    def __imul__(self, m):
        m = float(m)
        self[0] *= m
        self[1] *= m
    def __idiv__(self,d):
        d = float(d)
        self[0] /= d
        self[1] /= d
    def __repr__(self):
        return "[%.3f, %.3f]" % (self.x, self.y)
    def __getitem__(self,key):
        if (key==0):
            return self.x
        elif(key==1):
            return self.y
        else:
            raise Exception("invalid key")

def smooth(path, fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.00001):
    #
    # Enter code here. 
    # The weight for each of the two new equations should be 0.5 * weight_smooth
    #
    #deep copy into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]
    change = tolerance
    while change >= tolerance:
        for i in range(0,len(newpath)):
            if not fix[i]:
                xi = Point(path[i][0], path[i][1])
                yi = Point(newpath[i][0], newpath[i][1])
                yip = Point(newpath[(i+1)%len(newpath)][0], newpath[(i+1)%len(newpath)][1])
                yim = Point(newpath[(i-1)%len(newpath)][0], newpath[(i-1)%len(newpath)][1])
                yi2p = Point(newpath[(i+2)%len(newpath)][0], newpath[(i+2)%len(newpath)][1])
                yi2m = Point(newpath[(i-2)%len(newpath)][0], newpath[(i-2)%len(newpath)][1])
            
                alpha = weight_data * (xi - yi)
                yi += alpha
                beta = weight_smooth * (yip + yim - (2 * yi)) 
                yi += beta
                gamma = 0.5 * weight_smooth * ((2.0*yim) - yi2m - yi)
                yi += gamma
                delta = 0.5 * weight_smooth * ((2.0*yip) - yi2p - yi)
                yi += delta

                newpath[i][0] = yi[0]
                newpath[i][1] = yi[1]

                t = alpha + beta + gamma + delta
                change = abs(t[0]) + abs(t[1])
    return newpath



#thank you - EnTerr - for posting this on our discussion forum

newpath = smooth(path, fix)
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'

# --------------------------------------------------
# check if two numbers are 'close enough,'used in
# solution_check function.
#
def close_enough(user_answer, true_answer, epsilon = 0.03):
    if abs(user_answer - true_answer) > epsilon:
        return False
    return True

# --------------------------------------------------
# check your solution against our reference solution for
# a variety of test cases (given below)
#
def solution_check(newpath, answer):
    if type(newpath) != type(answer):
        print "Error. You do not return a list."
        return False
    if len(newpath) != len(answer):
        print 'Error. Your newpath is not the correct length.'
        return False
    if len(newpath[0]) != len(answer[0]):
        print 'Error. Your entries do not contain an (x, y) coordinate pair.'
        return False
    for i in range(len(newpath)): 
        for j in range(len(newpath[0])):
            if not close_enough(newpath[i][j], answer[i][j]):
                print 'Error, at least one of your entries is not correct.'
                return False
    print "Test case correct!"
    return True

# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

testpath1=[[0, 0], #fix
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]
testfix1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
answer1 = [[0, 0],
           [0.7938620981547201, -0.8311168821106101],
           [1.8579052986461084, -1.3834788165869276],
           [3.053905318597796, -1.5745863173084],
           [4.23141390533387, -1.3784271816058231],
           [5.250184859723701, -0.8264215958231558],
           [6, 0],
           [6.415150091996651, 0.9836951698796843],
           [6.41942442687092, 2.019512290770163],
           [6, 3],
           [5.206131365604606, 3.831104483245191],
           [4.142082497497067, 4.383455704596517],
           [2.9460804122779813, 4.5745592975708105],
           [1.768574219397359, 4.378404668718541],
           [0.7498089205417316, 3.826409771585794],
           [0, 3],
           [-0.4151464728194156, 2.016311854977891],
           [-0.4194207879552198, 0.9804948340550833]]

testpath2 = [[0, 0], # fix
             [2, 0],
             [4, 0], # fix
             [4, 2],
             [4, 4], # fix
             [2, 4],
             [0, 4], # fix
             [0, 2]]
testfix2 = [1, 0, 1, 0, 1, 0, 1, 0]
answer2 = [[0, 0],
           [2.0116767115496095, -0.7015439080661671],
           [4, 0],
           [4.701543905420104, 2.0116768147460418],
           [4, 4],
           [1.9883231877640861, 4.701543807525115],
           [0, 4],
           [-0.7015438099112995, 1.9883232808252207]]
solution_check(smooth(testpath1, testfix1), answer1)
solution_check(smooth(testpath2, testfix2), answer2)


