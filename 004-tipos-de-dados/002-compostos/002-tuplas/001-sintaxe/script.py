# Tuplas é uma coleção de dados ordenada de valores o qual é permitido conter
# diferentes tipos de dados, sendo organizados por índice, onde diferente de uma
# lista, seus elementos não podem ser alterados, adicionados ou deletados,
# pois seus elementos são imutáveis.

dados_imc = ('ROBSON ALVES FEIJÓ', [34, 81.55, 1.69], True, None)
print(dados_imc)
print(type(dados_imc))

# Exibindo um dado de uma tupla:
print(dados_imc[0])

# Realizando alteração em uma tupla:
dados_imc[2] = False
print(dados_imc)
# !NOTA¹: Será emitido um erro ao tentar alterar o elemento de uma tupla.
# !Se tentarmos adicionar ou remover, retornará um erro.

# TODOS FUNÇÕES		: São blocos de códigos reutilizáveis.
# print : Imprime dados na tela.
# type  : Verifica o tipo de dado.

# TODOS MÉTODOS		: São funções que estão associadas a um objeto.
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados em outros arquivos.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos com funcionalidades específicas. 
#       :