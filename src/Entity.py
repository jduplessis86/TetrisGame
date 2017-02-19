from enum import Enum

class Rotate(Enum):
	ClockWise = 1
	CClockWise = 2

class Entity(object):
	def _init_(self,hight,width,moveable):
		self.x = 0
		self.y = 0
		self.hight = hight
		self.width = width
		self.moveable = moveable
		self.shape = []


	def getShape(self):
		return self.shape

	def setShape(self, shape):
		self.shape = shape

	def move(self,deltaX,deltaY):
		self.x += deltaX
		self.y += deltaY

	def rotate(self, Rotate):
		pass
