
class SceneManager(object):
	def _init_(self,hight,width):
		entitys =[]
		image = []
		for x in range(hight):
			image.append([])
			for y in range(width):
				image[y].append('w')


	def addEntity(self,entity):
		entity.insert(entity)

	def updateScene(self):
		pass

	def drawScene(self):
		for x in len(image):
			print(str(image[x]).strip(',[]'))

