# This is where chapter 15 exercises go.

import copy


class Point(object):
	"""Represents a point in two-dimensional space"""

# a = Point()

# a.x = 2.0
# a.y = 3.0

# b = Point()


# b.x = 5
# b.y = 7


def print_point(pt):
	print "(%g, %g)" % (pt.x, pt.y)



class Rectangle(object):
	"""Represents a Rectangle

	attributes: width, height, corner"""


def print_rectangle(rect):
	print "The rectangle's lower left-hand corner is on", "(%g, %g)" % (rect.c.x, rect.c.y)
	print "The rectangle's width is", "%g" " units." % (rect.w)
	print "The rectangle's height is", "%g" " units." % (rect.h)

def find_center(rect):
	p = Point()
	p.x = rect.c.x + rect.w/2
	p.y = rect.c.y + rect.h/2
	return p



def grow_rectangle(rect, addwidth, addheight):
	rect.w += addwidth
	rect.h += addheight
	


def move_rectangle(rect, dx, dy):
	rect2 = copy.deepcopy(rect)
	rect2.c.x += dx
	rect2.c.y += dy
	return rect2


c = Rectangle()

c.w = 2

c.h = 4

c.c = Point()

c.c.x = 1.0

c.c.y = 1.0


print_rectangle(c)

d = move_rectangle(c, 10, 20)

print_rectangle(d)
