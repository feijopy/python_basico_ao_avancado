# São conjuntos de dados com valores únicos que não podem se repetir, porém,
# assim como listas e tuplas, é permitido conter diferentes tipos de dados. Por
# não ser ordenado, não é possível acessar elementos por índice.

dados_imc = {None, 34, 81.55, 'feijopy@gmail.com', True}
print(dados_imc)
print(type(dados_imc))

# Adicionando um elemento existente em um conjunto:
dados_imc.add(True)
print(dados_imc)
# !NOTA¹: Ao tentar adicionar elemento em um set, ele será ingnorado.
# !Se tentarmos acessar um elemento do set, retornará um erro.

# Adicionando um elemento inexistente em um conjunto:
dados_imc.add('Masculino')
print(dados_imc)

# TODOS FUNÇÕES		: São blocos de código que podem ser reutilizados.
# print : Imprime dados na tela.
# type  : Verifica o tipo de dado.

# TODOS MÉTODOS		: São funções que pertencem a uma classe. 
# add   : Adiciona elemento em um cojunto.

# TODOS MÓDULOS		: São arquivos que podem ser importados.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos que são disponibilizados 
#       :