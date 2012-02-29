colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def maxconfuse(world):
	#default probs
	p = []
	for i in range(len(world)):
		row = []
		for j in range(len(world[i])):
			row.append(1./(len(world)*len(world[i])))
		p.append(row)
	return p

def normalize(p):
	#normalizer
	#div by 0 risk here
	rsum = checkpsums(p)
	for i in range(len(p)):
		for j in range(len(p[i])):
			p[i][j] = p[i][j]/rsum
	return p

def checkpsums(p):
	#get probs sum
	rsum = 0
	for i in range(len(p)):
		rsum += sum(p[i])
	return rsum

def sense(p, color, accuracy):
	#sensing
	pHit = accuracy
	pMiss = 1 - accuracy
	q = []
	for i in range(len(p)):
		row = []
		for j in range(len(p[i])):
			hit = (color == colors[i][j])
			row.append(p[i][j]*(hit*pHit + (1-hit)*pMiss))
		q.append(row)
	q = normalize(q)
	return q

# 2d motion
# horizontal is in the inner lists
# vertical is in the outer lists -> u = left, d = right
def move(p, M, p_move):
	# M - [0,0]=no move, [0,1]=right, [1,0]=down (neg = other way)
	# p_move = % chance of motion, else no move
	moveH = M[1]
	moveV = M[0] #(up = left)
	q = []
	if moveH != 0:
		#horizontal motion
		for i in range(len(p)):
			q.append(minimove(p[i],moveH, p_move))
	elif moveV != 0:
		#vertical motion
		q = minimove(p, moveV, p_move)
	else:
		# no motion
		q = p
	return q

def minimove(p, U, p_move):
	q = []
	for i in range(len(p)):
		# if element of p is float, then this
		if type(p[i]) == float:
			s = p_move * p[(i-U)%len(p)]
			s = s + (1-p_move) * p[i]
			q.append(s)
		else:
			#assume it's a list, ugh this is fragile 
			s1 = map((lambda z: z*p_move),p[(i-U)%len(p)])
			s2 = map((lambda z: z*(1-p_move)),p[(i-U+1)%len(p)])
			s = [a + b for a, b in zip(s1,s2)]
			q.append(s)
	return q

# #OVERRIDES - for testing
# # world override
# colors = [['green','green','green','green'],
# 		['green','red','green','green'],
# 		['green','green','green','green']]
# #perfect sensor override
# sensor_right = 1.0
# #perfect motion override
# p_move = 1.0
# #measurements override 
# measurements = ['red','green']
# #motions override
# motions = [[0,0],[1,0]]

#initize probability grid
p = maxconfuse(colors)
#raise error if bad
assert(checkpsums(p)==1.0)

#move and measure
for k in range(len(measurements)):
	p = move(p, motions[k], p_move)
	p = sense(p, measurements[k], sensor_right)

#sanity check for bad probs
try:
	assert(checkpsums(p) == 1.0)
except:
	print "Bad Probabilities!"


#Your probability array must be printed 
#with the following code.

show(p)





