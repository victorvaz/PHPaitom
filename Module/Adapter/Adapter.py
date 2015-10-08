"""
Classe responsável por criar a conexão com o banco de dados em php
"""
class Adapter :
	"""
	Nome do arquivo
	"""
	fileName = 'Adapter'
	servidor = None # Caminho do servidor de banco de dados
	banco = None # Nome do banco de dados
	usuario = None # Nome de usuário do banco de dados
	senha = None # Senha do banco de dados

	"""
	Inicia uma classe Adapter
	"""
	def __init__ (self, servidor, banco, usuario, senha) :
		self.servidor = servidor
		self.banco = banco
		self.usuario = usuario
		self.senha = senha

	"""
	Gera a classe adapter
	"""
	def generate (self) :
		campos = {
			'{%__SERVIDOR__%}' : self.servidor,
			'{%__BANCO__%}' : self.banco,
			'{%__USUARIO__%}' : self.usuario,
			'{%__SENHA__%}' : self.senha
		}

		arquivo = open('Module/Adapter/adapter.template.php', 'r', encoding="utf8").read()

		for (nome, valor) in campos.items() :
			arquivo = arquivo.replace(nome, valor)

		return arquivo

	"""
	Retorna o nome do arquivo
	"""
	def __repr__ (self) :
		return self.fileName