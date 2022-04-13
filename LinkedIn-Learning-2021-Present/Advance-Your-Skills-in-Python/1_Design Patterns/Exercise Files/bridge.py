class DrawingAPIOne(object):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class DrawingAPITwo(object):
	"""Implementation-specific abstraction: concrete class two"""
	def draw_circle(self, x, y, radius): # implementation will be different
		print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))
		

class Circle(object):
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x # coordinates
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api # accepts instance

	def draw(self):
		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		"""Implementation-independent"""
		self._radius *= percent


#Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne()) # decides what kind of circle we're invoking
#Draw a circle
circle1.draw()

#Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())

#Draw a circle
circle2.draw()

