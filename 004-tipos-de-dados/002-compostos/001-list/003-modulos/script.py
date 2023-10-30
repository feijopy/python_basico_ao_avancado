# Lista de dados com uma coleção ordenada de valores o qual é permitido conter
# diferentes tipos de dados, sendo organizados por índice, onde seus elementos
# podem ser mutáveis.

dados_imc = [None, 34, 81.55, 'feijopy@gmail.com', True]
print(dados_imc)
print(type(dados_imc))

# Exibindo um dado da lista:
print(dados_imc[0])

# Adicionando dado em lista:
dados_imc.append('Masculino')
print(dados_imc)

# Deletando dado em uma lista:
del dados_imc[0]

# Realizando alteração em uma lista:
dados_imc[4] = False
print(dados_imc)


# TODOS FUNÇÕES		: São blocos de código que podem ser reutilizados.
# print   : Imprime dados na tela.
# type    : Verifica o tipo de dado.


# TODOS MÉTODOS		: São funções que pertencem a uma classe. 
# append  : Adiciona elemento na lista.
# del     : Deleta elemento especificado na lista.

# TODOS MÓDULOS		: São arquivos que podem ser importados.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos que são disponibilizados 
#       :