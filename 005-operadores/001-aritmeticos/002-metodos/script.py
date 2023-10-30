# Usado para realizarmos operações aritméticas.
# Abaixo seguem os mais utilizados por ordem de precedência:

# ** : Potenciação;
# *  : Multiplicação;
# /  : Divisão;
# %  : Resto da divisão;
# +  : Adição;
# -  : Subtração.
# !NOTA¹: Para evitarmos erros de cálculos, usamos os parênteses para burla a
# !ordem de precedência.

dados_imc = {
	'email': 'feijopy@gmail.com',
	'sexo': 'Masculino',
	'idade': 34,
	'peso': 81.55,
	'altura': 1.69,
	'imc': None,
}

resultado_imc = round(dados_imc['peso'] / (dados_imc['altura'] * dados_imc['altura']), 2)

print(f'IMC: {resultado_imc}')

# TODOS FUNÇÕES		: São blocos de código que podem ser reutilizados.
# print : Imprime dados na tela.
# round : Arredonda número para casa decimal estipulada.

# TODOS MÉTODOS		: São funções que pertencem a uma classe. 
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos que são disponibilizados 
#       :
