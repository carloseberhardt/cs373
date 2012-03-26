from math import *

path = [[0,0],
        [0,1],
        [0,2],
        [1,2],
        [2,2],
        [3,2],
        [4,2],
        [4,3],
        [4,4]]

def smooth(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):
    #deep copy into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]
    change = True
    while change:
        change = False
        for i in range(1,len(newpath)-1):
            xi = Point(path[i][0], path[i][1])
            yi = Point(newpath[i][0], newpath[i][1])
            yip = Point(newpath[i+1][0], newpath[i+1][1])
            yim = Point(newpath[i-1][0], newpath[i-1][1])
            alpha = weight_data * (xi - yi)
            #yi = yi + alpha
            beta = weight_smooth * (yip + yim - (2 * yi))
            #yi = yi + beta
            yi = yi + alpha + beta
            newpath[i][0] = yi[0]
            newpath[i][1] = yi[1]
            t = alpha + beta
            tot = abs(t[0]) + abs(t[1])
            if tot > tolerance:
                change = True

    return newpath

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



newpath = smooth(path)

for i in range(len(path)):
    print '[' + ', '.join('%.6f' % x for x in path[i]) + '] -> [' + ','.join('%.6f' % x for x in newpath[i]) + ']'
