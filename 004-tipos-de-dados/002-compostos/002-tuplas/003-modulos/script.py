# Tuplas é uma coleção de dados ordenada de valores o qual é permitido conter
# diferentes tipos de dados, sendo organizados por índice, onde diferente de uma
# lista, seus elementos não podem ser alterados, adicionados ou deletados,
# pois seus elementos são imutáveis.

dados_imc = (None, 34, 81.55, 'feijopy@gmail.com', True)
print(dados_imc)
print(type(dados_imc))

# Exibindo um dado de uma tupla:
print(dados_imc[0])

# Realizando alteração em uma tupla:
dados_imc[4] = False
print(dados_imc)
# !NOTA¹: Será emitido um erro ao tentar alterar o elemento de uma tupla.
# !Se tentarmos adicionar ou remover, retornará um erro.

# TODOS FUNÇÕES		: São blocos de código que podem ser reutilizados.
# print : Imprime dados na tela.
# type  : Verifica o tipo de dado.

# TODOS MÉTODOS		: São funções que pertencem a uma classe. 
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos que são disponibilizados 
#       :