import math
def is_inside(x1, y1, x2, y2, x3, y3, ax, ay):
	a= abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0)
	a1= abs((x1*(y2-ay) + x2*(ay-y1)+ ax*(y1-y2))/2.0)
	a2= abs((x2*(y3-ay) + x3*(ay-y2)+ ax*(y2-y3))/2.0)
	a3= abs((x1*(y3-ay) + x3*(ay-y1)+ ax*(y1-y3))/2.0)
	return a==(a1+a2+a3)

def found(x1, y1, x2, y2, x3, y3, px, py, bx, by):
	d1= math.sqrt((x1-x2)**2 + (y1-y2)**2)
	d2= math.sqrt((x2-x3)**2 + (y2-y3)**2)
	d3= math.sqrt((x1-x3)**2 + (y1-y3)**2)
	if d1 + d2 <= d3 and d2 + d3 <= d1 and d3 + d1 <= d2:
		return 0
	planeInside= is_inside(x1, y1, x2, y2, x3, y3, px, py)
	boatInside= is_inside(x1, y1, x2, y2, x3, y3, bx, by)
	if planeInside:
		if boatInside:
			return 3
		return 1
	else:
		if boatInside:
			return 2
		return 4

print found(3,1,7,1,5,5,3,1,0,0)

