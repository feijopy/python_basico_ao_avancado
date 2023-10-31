# São conjuntos de dados com valores únicos que não podem se repetir, porém,
# assim como listas e tuplas, é permitido conter diferentes tipos de dados. Por
# não ser ordenado, não é possível acessar elementos por índice.

dados_imc = {'ROBSON ALVES FEIJÓ'}
print(dados_imc)

# Adicionando um elemento existente em um conjunto:
dados_imc.add('ROBSON ALVES FEIJÓ')
print(dados_imc)
# !NOTA¹: Ao tentar adicionar elemento em um set, ele será ingnorado.
# !Se tentarmos acessar um elemento do set, retornará um erro.

# Adicionando um elemento inexistente em um conjunto:
dados_imc.add('RAQUEL COSTA LIMA')
print(dados_imc)

# TODOS FUNÇÕES		: São blocos de códigos reutilizáveis.
# print : Imprime dados na tela.

# TODOS MÉTODOS		: São funções que estão associadas a um objeto.
# add   : Adiciona elemento em um cojunto.

# TODOS MÓDULOS		: São arquivos que podem ser importados em outros arquivos.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos com funcionalidades específicas. 
#       :