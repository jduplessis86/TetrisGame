
class SceneManager(object):
	def __init__(self,hight,width):
		self.entitys =[]
		self.image = []
		for x in range(hight):
			self.image.append([])
			for y in range(width):
				self.image[x].append('w')


	def addEntity(self,entity):
		self.entity.insert(entity)

	def updateScene(self):
		pass

	def drawScene(self):
		for index,val in enumerate(self.image):
			print(str(self.image[index]).strip(',[]'))


