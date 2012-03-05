
def split(coco):
	return (coco-1) % 5

startx = 6.
men = 6
x = startx

print "men: %s, startx: %s, x: %s" % (men, startx, x)

while men > 0:
	if (x-1)%5 == 0:
		x = x * 5. / 4. + 1
		if x % 1 != 0:
			men = 6
			startx += 5
			x = startx
	else:
		men = 6
		startx += 5
		x = startx
	men -= 1

print "men: %s, startx: %s, x: %s" % (men, startx, x)
