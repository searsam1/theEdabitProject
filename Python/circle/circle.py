import math
def circle(n):
	
	a,b = 50/math.pi,50/math.pi

	theta = math.radians(360 / n)
	c = math.pow( (b**2) + (a**2) - (2*a*b) * (math.cos(theta)), .5 )
	
	perimeter = c * n
	return round(perimeter,3)

circle(3)
