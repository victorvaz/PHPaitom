from Module.Entity.Atributo import Atributo
from Module.Metodo.Metodo import Metodo

class Model :
	"""
	Classe responsável por gerar a classe modelo para uma determinada entidade.
	"""
	entidade = None # Entidade referente à classe modelo

	def __init__ (self, entidade) :
		"""
		Construtor da classe.
		"""
		self.entidade = entidade

	def createMetodoCadastrar (self) :
		"""
		Cria o método cadastrar
		"""
		r = "\n\tpublic static function cadastrar(%s $%s) {\n" % (self.entidade.nomeEntidade, self.entidade.nomeEntidade)

		campos = []
		for atributo in self.entidade.atributos :
			if atributo.isPrimaryKey != True :
				campos.append(atributo.nome)

		r += "\t\tAdapter::query(\"INSERT INTO %s (%s)" % (self.entidade.nomeEntidade.lower(), ', '.join(campos))

		campos = []
		for atributo in self.entidade.atributos :
			if atributo.isPrimaryKey != True :
				campos.append("'{$%s->%s}'" % (self.entidade.nomeEntidade, atributo.nome))

		r += " VALUES (%s);\");\n\t}\n" % ', '.join(campos)
		return r

	def createMetodoAtualizar (self) :
		"""
		Cria o método atualizar
		"""
		r = "\n\tpublic static function atualizar(%s $%s) {\n" % (self.entidade.nomeEntidade, self.entidade.nomeEntidade)

		campos = []
		for atributo in self.entidade.atributos :
			if atributo.isPrimaryKey != True :
				campos.append("%s = {$%s->%s}" % (atributo.nome, self.entidade.nomeEntidade, atributo.nome) if (atributo.tipo == Atributo.TYPE_INT) else "%s = '{$%s->%s}'" % (atributo.nome, self.entidade.nomeEntidade, atributo.nome))

		r += "\t\tAdapter::query(\"UPDATE %s SET %s" % (self.entidade.nomeEntidade.lower(), ', '.join(campos))

		campoPrimaryKey = self.entidade.getPrimaryKey()
		if campoPrimaryKey != "" :
			r += " WHERE %s = {$%s->%s}" % (campoPrimaryKey, self.entidade.nomeEntidade, campoPrimaryKey)

		r += "\");\n\t}\n";
		return r

	def createMetodoDeletar (self) :
		"""
		Cria o método deletar
		"""
		campoPrimaryKey = self.entidade.getPrimaryKey()
		r = "\n\tpublic static function deletar($%s) {\n" % campoPrimaryKey
		r += "\t\tAdapter::query(\"DELETE FROM %s WHERE %s = {$%s}\");\n\t}\n" % (self.entidade.nomeEntidade.lower(), campoPrimaryKey, campoPrimaryKey)
		return r

	def createMetodoBuscar (self) :
		"""
		Cria o método buscar principal
		"""
		campos = []
		for atributo in self.entidade.atributos :
			campos.append(atributo.nome)

		r = "\n\tprivate static function buscar() {\n"
		r += "\t\t$query = Adapter::query(\"SELECT %s FROM %s \" . (func_num_args() > 0 ? \" WHERE \" . implode(\" AND \", func_get_args()) : \"\"));\n" % (', '.join(campos), self.entidade.nomeEntidade.lower())
		r += "\t\t$list = array();\n"
		r += "\t\twhile ($row = mysqli_fetch_array($query))\n"

		campos = []
		for atributo in self.entidade.atributos :
			campos.append("$row['%s']" % atributo.nome)

		r += "\t\t\t$list[] = new %s(%s);\n" % (self.entidade.nomeEntidade, ', '.join(campos))
		r += "\t\treturn $list;\n\t}\n"
		return r

	def createMetodoBuscarPorPrimaryKey (self) :
		"""
		Cria o método buscar por ID
		"""
		campoPrimaryKey = self.entidade.getPrimaryKey()
		r = "\n\tpublic static function buscarPorID($%s) {\n" % campoPrimaryKey
		r += "\t\treturn static::buscar(\"%s = {$%s}\")[0];\n" % (campoPrimaryKey, campoPrimaryKey)
		r += "\t}\n"
		return r

	def createMetodoBuscarTodos (self) :
		"""
		Cria o método buscar todos
		"""
		return "\n\tpublic static function buscarTodos() {\n\t\treturn static::buscar();\n\t}\n"

	def generate (self) :
		"""
		Metodo para gerar a classe modelo
		"""
		campos = {
			# Coloca o nome da entidade:
			'{%__NOME_ENTIDADE__%}' : self.entidade.nomeEntidade,
			# Cria o método cadastrar se for necessário:
			'{%__METODO_CADASTRAR__%}' : self.createMetodoCadastrar() if self.entidade.haveCadastrar else '',
			# Cria o método atualizar se for necessário:
			'{%__METODO_ATUALIZAR__%}' : self.createMetodoAtualizar() if self.entidade.haveAtualizar else '',
			# Cria o método deletar se for necessário:
			'{%__METODO_DELETAR__%}' : self.createMetodoDeletar() if self.entidade.haveDeletar else '',
			# Cria os métodos de busca se for necessário:
			'{%__METODO_BUSCAR__%}' : self.createMetodoBuscar() if self.entidade.haveBuscar else '',
			'{%__METODO_BUSCAR_POR_PRIMARY_KEY__%}' : self.createMetodoBuscarPorPrimaryKey() if self.entidade.haveBuscar else '',
			'{%__METODO_BUSCAR_TODOS__%}' : self.createMetodoBuscarTodos() if self.entidade.haveBuscar else '',
			'{%__METODOS_EXTRAS__%}' : '\n\n'.join(self.entidade.metodosExtras)
		}

		arquivo = open('Module/Model/model.template.php', 'r', encoding="utf8").read()

		for (nome, valor) in campos.items() :
			arquivo = arquivo.replace(nome, valor)

		return arquivo

	def __repr__ (self) :
		return self.generate()