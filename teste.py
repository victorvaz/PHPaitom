# importa dependências
from Compiler import Compiler
from Module.Module import Module # Modulo (Geral)
from Module.Adapter.Adapter import Adapter # Adapter (Core)
from Module.Entity.Entity import Entity # Entity (MVC)
from Module.Entity.Entity import Atributo # Entity (MVC)

# Adaptador de Banco de Dados
adapter = Adapter('localhost', 'testebd', 'root', '')

# Modulo Core
core = Module('Core')
core.addFiles(adapter)

# Modulo Carros
entCarro = Entity('Carro')
entCarro.addAtributos(
	Atributo('id', Atributo.TYPE_INT, None, True, True, True, False),
	Atributo('nome', Atributo.TYPE_VARCHAR, 180),
	Atributo('modelo', Atributo.TYPE_VARCHAR, 100),
	Atributo('marca', Atributo.TYPE_VARCHAR, 100),
	Atributo('placa', Atributo.TYPE_VARCHAR, 100),
	Atributo('cor', Atributo.TYPE_VARCHAR, 100)
)
entCarro.createModel()
entCarro.generateCreateTable()

modCarros = Module('Carros')
modCarros.addFiles(entCarro)

# Compila o resultado
compilador = Compiler('teste_compilador')
compilador.addModules(core, modCarros)
compilador.generate()

print("Compilado")