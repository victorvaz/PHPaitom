from Module.Table.Table import Table

class Init :
	"""
	Classe responsável por criar o auto-load de cada módulo para que estes possam ser incluído com menos atrito.
	"""
	nomeModulo = None # Nome do módulo
	autor = None # Autor do módulo
	emailAutor = None # E-mail do autor do módulo
	data = None # Data de criação do módulo
	dependencias = None # Dependências do módulo
	entidadesComTabela = None # Entidades que terão tabela.

	def __init__ (self, nomeModulo, autor = '', emailAutor = '', data = '', dependencias = []) :
		"""
		Construtor da classe.
		"""
		self.nomeModulo = nomeModulo
		self.autor = autor
		self.emailAutor = emailAutor
		self.data = data
		self.entidadesComTabela = []
		self.dependencias = []
		for d in dependencias :
			self.dependencias.append(d)

	def createTable (self, *args) :
		"""
		Cria as tabelas para as entidades informadas
		"""
		for e in args :
			self.entidadesComTabela.append(e)

	def addDependencias (self, *args) :
		"""
		Método para adicionar dependencias dos módulos
		"""
		for d in args :
			self.dependencias.append(d)

	def generate(self) :
		"""
		Gera o arquivo init
		"""
		r = '<?php\n\n'

		# Informa o nome do módulo caso necessário:
		if self.nomeModulo != '' :
			r += '// Módulo %s.\n' % self.nomeModulo

		# Informa o nome do author caso necessário:
		if self.autor != '' :
			r += '// Autor: %s <%s>\n' % (self.autor, self.emailAutor if self.emailAutor != '' else '')

		# Informa a data do módulo caso necessário:
		if self.data != '' :
			r += '// Data: %s' % data

		r += '\n// Dependências:\n'

		for a in self.dependencias :
			r += "include '%s';\n" % a

		for e in self.entidadesComTabela :
			r += Table(e).generate()

		r += "?>"
		return r

	def __repr__ (self) :
		return self.generate()