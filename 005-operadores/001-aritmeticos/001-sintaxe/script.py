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
    'Nome': 'ROBSON ALVES FEIJÓ',
	'Sexo': 'Masculino',
	'Idade': 34,
	'Altura': 1.69,
	'Peso': 81.55,
	'IMC': None,
    'Acima do peso': None
}

resultado_imc = round(dados_imc['Peso'] / (dados_imc['Altura'] * dados_imc['Altura']), 2)

print(f'IMC: {resultado_imc}')

# TODOS FUNÇÕES		: São blocos de códigos reutilizáveis.
# print : Imprime dados na tela.
# round : Arredonda número para casa decimal estipulada.

# TODOS MÉTODOS		: São funções que estão associadas a um objeto.
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados em outros arquivos.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos com funcionalidades específicas. 
#       :
