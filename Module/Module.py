class Module :

	def __init__ (self, name) :
		self.name = name

	def addFiles(self, *args) :
		self.files = args

	def __repr__ (self) :
		return self.name