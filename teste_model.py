from Module.Compiler.Compiler import Compiler
from Module.Module import Module
from Module.Adapter.Adapter import Adapter
from Module.Entity.Atributo import Atributo
from Module.Entity.Entity import Entity
from Module.Metodo.Metodo import Metodo

entCarro = Entity('Carro')
entCarro.addAtributos(
	Atributo('id', Atributo.TYPE_INT, None, True, True, True, False),
	Atributo('nome', Atributo.TYPE_VARCHAR, 180),
	Atributo('modelo', Atributo.TYPE_VARCHAR, 100),
	Atributo('marca', Atributo.TYPE_VARCHAR, 100),
	Atributo('placa', Atributo.TYPE_VARCHAR, 100),
	Atributo('cor', Atributo.TYPE_VARCHAR, 100)
)
entCarro.createModel(
	metodos = [
		Metodo('buscarPorNomeMarca', ['nome', 'marca'], \
			"return $this->buscar(\"nome = '{$nome}'\", \"marca = '{$marca}'\")[0];\
return $this->buscar(\"nome = '{$nome}'\", \"marca = '{$marca}'\")[0];\
return $this->buscar(\"nome = '{$nome}'\", \"marca = '{$marca}'\")[0];\
return $this->buscar(\"nome = '{$nome}'\", \"marca = '{$marca}'\")[0];\
return $this->buscar(\"nome = '{$nome}'\", \"marca = '{$marca}'\")[0];", True)
	]
)

modCarros = Module('Carros')
modCarros.addFiles(entCarro)

comp = Compiler('teste_model')
comp.addModules(modCarros)
comp.generate()

print('Compilado')