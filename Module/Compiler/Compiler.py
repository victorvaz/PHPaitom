# -*- coding: utf-8 -*-
import os
from datetime import date
from Module.Entity.Entity import Entity
from Module.Init.Init import Init

class Compiler :
	"""
	Compilador do programa. Responsável por gerar o código em PHP.
	"""
	diretorio = None # Diretório de construção do programa.
	author = None # Autor do programa.
	emailAutor = None # E-mail do autor do programa.
	modules = None # Módulos do programa.
	
	def __init__ (self, diretorio, author = 'Víctor Vaz', emailAutor = 'victor@operacaosistemas.com.br') :
		"""
		Construtor da classe.
		"""
		self.diretorio = diretorio
		self.author = author
		self.emailAutor = emailAutor
		self.modules = {}

	def addModules(self, *args) :
		"""
		Adiciona os módulos ao programa.
		"""
		self.modules = args

	def generate(self) :
		"""
		Método para gerar o módulo.
		"""
		# Apaga a pasta onde serão salvos os arquivos:
		if os.path.isdir(self.diretorio) :
			os.system("rd %s /s /q" % self.diretorio)

		# Cria novamente a pasta:
		os.mkdir(self.diretorio)

		# Cria a pasta 'Module':
		os.mkdir('%s/Module' % self.diretorio)

		# Cria os módulos dentro da pasta 'diretorio/Module':
		for module in self.modules :
			# Cria a pasta do módulo:
			os.mkdir('%s/Module/%s' % (self.diretorio, module))

			# Cria o arquivo init:
			init = Init(self.author, self.emailAutor, '%i/%i/%i' % (date.today().day, date.today().month, date.today().year))

			# Cria os arquivos do módulo:
			for arquivo in module.files :
				# Cria o arquivo da entidade do módulo:
				arqEntidade= open('%s/Module/%s/%s' % (self.diretorio, module, "%s.php" % arquivo), 'w', encoding="utf8")
				arqEntidade.write(arquivo.generate())
				arqEntidade.close()

				# Adiciona o arquivo ao init do módulo:
				init.addDependencias('%s.php' % arquivo)

				# Cria o arquivo modelo caso exista
				if (type(arquivo) == type(Entity(""))) :
					if (arquivo.haveModel) :
						arqModel = open('%s/Module/%s/%s' % (self.diretorio, module, "%sModel.php" % arquivo), 'w', encoding="utf8")
						arqModel.write(arquivo.generateModel())
						arqModel.close()

						# Adiciona o arquivo ao init do módulo:
						init.addDependencias('%sModel.php' % arquivo)

				# Cria o auto create table
				if (type(arquivo) == type(Entity(""))) :
					init.createTable(arquivo)

			# Cria um arquivo init para o módulo:
			arqInit = open('%s/Module/%s/__init__.php' % (self.diretorio, module), 'a', encoding="utf8")
			arqInit.write(init.generate())
			arqInit.close()