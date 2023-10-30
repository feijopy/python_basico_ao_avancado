# Dicionários são uma coleção de pares chave-valor, onde estão ordenadas e cada
# chave está associada a um valor. Assim como listas e tuplas, também é
# permitido conter diferentes tipos de dados, porém suas chaves imutáveis.
# Seus dados são acessados por suas chaves e não índices.

dados_imc = {
	'email': 'feijopy@gmail.com',
	'sexo': 'Masculino',
	'idade': 34,
	'peso': 81.55,
	'altura': 1.69,
	'imc': None,
}

print(dados_imc)
print(type(dados_imc))

# Exibindo um dado de um dicionário:
print(dados_imc['email'])

# Adicionando dado em um dicionário:
dados_imc['nome'] = 'ROBSON ALVES FEIJÓ'
print(dados_imc)

# Deletando dado de um dicionário:
del dados_imc['nome']
print(dados_imc)

# Realizando alteração de um dicionário:
dados_imc['altura'] = 1.67
print(dados_imc)

# TODOS FUNÇÕES		: São blocos de código que podem ser reutilizados.
# print : Imprime dados na tela.
# type  : Verifica o tipo de dado.

# TODOS MÉTODOS		: São funções que pertencem a uma classe. 
# del   : Deleta elemento especificado na lista.

# TODOS MÓDULOS		: São arquivos que podem ser importados.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos que são disponibilizados 
#       :