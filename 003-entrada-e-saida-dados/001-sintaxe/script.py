# Normalmente os programas seguem o fluxo composto por três etapas.

# 1º ENTRADA        : Inserção dos dados.
# 2º PROCESSAMENTO  : Tratamento dos dados recebidos.
# 3º SAÍDA          : Resposta dos dados recebidos.

# Entrada dos dados:
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

# Processamento dos dados:
nome_completo = nome + ' ' + sobrenome


# ?JUNTAR CARACTERES:
# Para juntarmos as variáveis, fazemos a concatenação de strings, essa prática é
# chamada de interpolação. Em Python colocamos um "f" ou "F" antes das aspas,
# onde incorporamos as variáveis diretamente no texto delimitando por chaves.

# Saída dos dados:
print(f'Seja bem-vindo {nome_completo}!')

# TODOS FUNÇÕES		: São blocos de códigos reutilizáveis.
# input : Recebe dados do usuário.
# print : Imprime dados na tela.

# TODOS MÉTODOS		: São funções que estão associadas a um objeto.
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados em outros arquivos.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos com funcionalidades específicas. 
#       :