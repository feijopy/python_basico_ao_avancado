# Dicionários são uma coleção de pares chave-valor, onde estão ordenadas e cada
# chave está associada a um valor. Assim como listas e tuplas, também é
# permitido conter diferentes tipos de dados, porém suas chaves são imutáveis.
# Para acessar seus elementos, é usado chaves em vezde índices.

dados_imc = {
    'Nome': 'ROBSON ALVES FEIJÓ',
	'Sexo': 'Masculino',
	'Idade': 34,
	'Altura': 1.69,
	'Peso': 81.55,
	'IMC': None,
    'Acima do peso': None
}

print(dados_imc)
print(type(dados_imc))

# Exibindo um dado de um dicionário:
print(dados_imc['Nome'])

# Adicionando dado em um dicionário:
dados_imc['Qtde kcal'] = None
print(dados_imc)

# Realizando alteração de um dicionário:
dados_imc['Altura'] = 1.67
print(dados_imc)

# TODOS FUNÇÕES		: São blocos de códigos reutilizáveis.
# print : Imprime dados na tela.
# type  : Verifica o tipo de dado.

# TODOS MÉTODOS		: São funções que estão associadas a um objeto.
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados em outros arquivos.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos com funcionalidades específicas. 
#       :