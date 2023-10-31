# Dicionários são uma coleção de pares chave-valor, onde estão ordenadas e cada
# chave está associada a um valor. Assim como listas e tuplas, também é
# permitido conter diferentes tipos de dados, porém suas chaves imutáveis.
# Seus dados são acessados por suas chaves e não índices.

dados_imc = {
    'Nome': 'ROBSON ALVES FEIJÓ',
	'Sexo': 'Masculino',
	'Idade': 34,
	'Altura': 1.69,
	'Peso': 81.55,
	'IMC': None,
    'Acima do peso': None
}

# Deletando dado de um dicionário:
print(dados_imc)
del dados_imc['IMC']
del dados_imc['Acima do peso']
print(dados_imc)

# TODOS FUNÇÕES		: São blocos de códigos reutilizáveis.
# print : Imprime dados na tela.

# TODOS MÉTODOS		: São funções que estão associadas a um objeto.
# del   : Deleta elemento especificado na lista.

# TODOS MÓDULOS		: São arquivos que podem ser importados em outros arquivos.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos com funcionalidades específicas. 
#       :