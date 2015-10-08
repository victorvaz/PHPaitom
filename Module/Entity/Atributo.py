class Atributo :
	"""
	Classe que representa a abstração de um atributo
	"""
	# Constante de tipos de atributo
	TYPE_INT = "INT" # inteiro
	TYPE_DOUBLE = "DOUBLE" # double
	TYPE_VARCHAR = "VARCHAR" # varchar
	TYPE_TEXT = "TEXT" # texto
	TYPE_DATE = "DATE" # data
	TYPE_DATETIME = "DATETIME" # datetime
	TYPE_TIME = "TIME" # time

	nome = None # Nome do atributo
	tipo = None # Tipo do atributo
	tamanho = None # Tamanho do atributo
	isPrimaryKey = None # Se é PK
	isUnsigned = None # Se é Unsigned
	isAutoIncrement = None # Se é auto incremental
	isNull = None # Se é nulo

	def __init__ (self, nome, tipo, tamanho = None, isPrimaryKey = False, isUnsigned = False, isAutoIncrement = False, isNull = False) :
		"""
		Inicia a classe
		"""
		self.nome = nome
		self.tipo = tipo
		self.tamanho = 250 if (tipo == Atributo.TYPE_VARCHAR and tamanho == None) else tamanho
		self.isPrimaryKey = isPrimaryKey
		self.isUnsigned = isUnsigned
		self.isAutoIncrement = isAutoIncrement
		self.isNull = isNull

	def __repr__ (self) :
		"""
		Retorna o nome do atributo
		"""
		return self.nome