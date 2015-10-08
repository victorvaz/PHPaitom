import string

class Metodo :
	"""
	Classe para implementação de métodos para classes.
	"""
	nome = None # Nome do método.
	argumentos = None # Argumentos da classe.
	corpo = None # Corpo do método.
	isPrivate = False # Se o método é privado.
	isStatic = False # Se o método é estático.

	def __init__ (self, nome, argumentos, corpo, isStatic = False, isPrivate = False) :
		"""
		Construtor da classe.
		"""
		self.nome = nome
		self.corpo = corpo
		self.isStatic = isStatic
		self.isPrivate = isPrivate

		self.argumentos = []
		for a in argumentos :
			self.argumentos.append("$%s" % a)

	def generate (self) :
		"""
		Método para gerar o método.
		"""
		r = "\n\t"
		r += "private" if self.isPrivate else "public"
		
		if self.isStatic :
			r += " static"

		r += " function %s(%s) {\n" % (self.nome, ', '.join(self.argumentos))

		r += "\t\t%s\n\t}\n" % (';\n\t\t'.join(self.corpo.split(';')))

		return r

	def __repr__ (self) :
		return self.generate()