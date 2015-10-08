class Table :
	"""
	Classe que representa uma tabela no banco de dados.
	"""
	entidade = None # Entidade na qual a tabela está relacionada.

	def __init__ (self, entidade) :
		"""
		Construtor da classe.
		"""
		self.entidade = entidade

	def generate (self):
		"""
		Método para gerar a criação da tabela da entidade automaticamente
		"""
		r = "\n// Cria a tabela caso não exista:\n"
		r += "Adapter::query(\"CREATE TABLE IF NOT EXISTS %s (\n" % self.entidade.nomeEntidade.lower()

		ct = []
		for a in self.entidade.atributos :
			ct.append("\t\t\t\t\t%s %s%s%s%s%s" % (
				a,
				a.tipo,
				"" if a.tamanho == None else "(%s)" % a.tamanho,
				" UNSIGNED" if a.isUnsigned else "",
				" AUTO_INCREMENT" if a.isAutoIncrement else "",
				" NOT NULL" if a.isNull == False else ""
			))

		r += ',\n'.join(ct)
		r += ",\n\t\t\t\t\tPRIMARY KEY (%s)" % self.entidade.getPrimaryKey()
		r += "\n\t\t\t\t);\");\n\n"

		return r

	def __repr__ (self) :
		return self.generate()