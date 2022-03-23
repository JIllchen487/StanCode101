"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.graphics.gobjects import GPolygon
from campy.gui.events.timer import pause

# Constants
ORDER = 6  # Controls the order of Sierpinski Triangle
LENGTH = 600  # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150  # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100  # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950  # The width of the GWindow
WINDOW_HEIGHT = 700  # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""

	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: Controls the order of Sierpinski Triangle
	:param length: The length of order 1 Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of order 1 Sierpinski Triangle
	:return: Nonethiing (draw a sierpinski triangle based on the parameters
	"""
	n = order

	# Get x, y of other vertexes
	upper_right_x = upper_left_x + length
	upper_right_y = upper_left_y
	lower_x = upper_left_x + 0.5 * length
	lower_y = upper_left_y + 0.866 * length

	# Draw a big triangle
	big = GPolygon()
	big.add_vertex((upper_left_x, upper_left_y))
	big.add_vertex((upper_right_x, upper_right_y))
	big.add_vertex((lower_x, lower_y))

	window.add(big)

	# Gat the upper left x,y of small triangles
	upperleft_x_upperright = upper_left_x+(length/2)
	upperleft_y_upperright = upper_left_y
	upperleft_x_lower = lower_x - 0.5*(length/2)
	upperleft_y_lower = lower_y - 0.866*(length/2)

	if n > 1:
		# upper_left
		sierpinski_triangle(n-1, length/2, upper_left_x, upper_left_y)
		# upper_right
		sierpinski_triangle(n-1, length/2, upperleft_x_upperright, upperleft_y_upperright)
		# bottom
		sierpinski_triangle(n-1, length/2, upperleft_x_lower, upperleft_y_lower)



if __name__ == '__main__':
	main()
