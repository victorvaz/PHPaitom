from Module.Entity.Atributo import Atributo
from Module.Model.Model import Model

class Entity :
	"""
	Classe responsável por criar entidades
	"""
	nomeEntidade = None # Nome da entidade
	atributos = None # Atributos da entidade
	haveModel = None # Se a entidade possui uma classe modelo
	haveCadastrar = None # Se a classe modelo possui o método cadastrar
	haveAtualizar = None # Se a classe modelo possui o método atualizar
	haveDeletar = None # Se a classe modelo possui o método deletar
	haveBuscar = None # Se a classe modelo possui o método buscar
	metodosExtras = None # Lista de métodos extra

	def __init__ (self, nomeEntidade) :
		"""
		Construtor da classe
		"""
		self.nomeEntidade = nomeEntidade
		self.atributos = []
		self.haveModel = False
		self.haveCadastrar = False
		self.haveAtualizar = False
		self.haveDeletar = False
		self.haveBuscar = False
		self.metodosExtras = []

	def addAtributos (self, *args) :
		"""
		Adiciona os atributos da entidade
		"""
		for a in args :
			self.atributos.append(a)

	def createModel (self, haveCadastrar = True, haveAtualizar = True, haveDeletar = True, haveBuscar = True, **kargs) :
		"""
		Método para indicar que a entidade possui uma classe modelo
		"""
		self.haveModel = True
		self.haveCadastrar = haveCadastrar
		self.haveAtualizar = haveAtualizar
		self.haveDeletar = haveDeletar
		self.haveBuscar = haveBuscar

		if 'metodos' in kargs :
			for m in kargs['metodos'] :
				self.metodosExtras.append(m.generate())
			

	def generateAtributos (self) :
		"""
		Método para gerar os atributos da classe
		"""
		r = ""
		for a in self.atributos :
			r += "public $%s;\n\t" % a
		return r

	def generateArgumentosConstrutor (self) :
		"""
		Método para gerar os argumentos do construtor
		"""
		at = []
		for a in self.atributos :
			at.append("$%s = null" % a)

		return ', '.join(at)

	def generateSetAtributos (self) :
		"""
		Método para gerar o set dos atributos no construtor
		"""
		r = ""
		for a in self.atributos :
			r += "\t\t$this->%s = $%s;\n" % (a, a)
		return r

	def getPrimaryKey (self) :
		"""
		Retorna a chave primária da entidade
		"""
		pk = ""
		for a in self.atributos :
			if a.isPrimaryKey :
				pk = a.nome
		return pk

	def generate (self) :
		"""
		Gera a classe Entidade
		"""
		campos = {
			# Informa o nome da entidade
			'{%__NOME_ENTIDADE__%}' : self.nomeEntidade,
			# Cria os atributos da entidade
			'{%__ATRIBUTOS__%}' : self.generateAtributos(),
			# Cria os argumentos do contrutor e as definições de váriaveis:
			'{%__ARGUMENTOS_CONSTRUTOR__%}' : self.generateArgumentosConstrutor(),
			'{%__SET_ATRIBUTOS__%}' : self.generateSetAtributos()
		}

		arquivo = open('Module/Entity/entity.template.php', 'r', encoding="utf8").read()

		for (nome, valor) in campos.items() :
			arquivo = arquivo.replace(nome, valor)

		return arquivo

	def generateModel (self) :
		"""
		Método para gerar a classe modelo para a entidade
		"""
		return Model(self).generate()

	def __repr__ (self) :
		"""
		Retorna o nome da entidade
		"""
		return self.nomeEntidade