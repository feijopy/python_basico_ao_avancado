/**
 * Executa um determinado bloco de código caso a condição seja satisfeita.
 * Normalmente usado quando temos determinadas condições a serem satisfeitas.
 */

function resultadoImc (peso, altura, imc) {
  imc = peso / (altura * altura)

  switch (true) {
    case imc < 18.50:
      return `Peso: ${peso} kg\nAltura: ${altura} cm \nIMC: ${imc.toFixed(2)}\nResultado: Abaixo do peso normal.`
      break
    case imc >= 18.50 && imc <= 24.99:
      return `Peso: ${peso} kg\nAltura: ${altura} cm \nIMC: ${imc.toFixed(2)}\nResultado: Peso normal.`
      break
    case imc >= 25.00 && imc <= 29.99:
      return `Peso: ${peso} kg\nAltura: ${altura} cm \nIMC: ${imc.toFixed(2)}\nResultado: Sobrepeso.`
      break
    case imc >= 30.00 && imc <= 34.99:
      return `Peso: ${peso} kg\nAltura: ${altura} cm \nIMC: ${imc.toFixed(2)}\nResultado: Obesidade Grau I.`
      break
    case imc >= 35.00 && imc <= 39.99:
      return `Peso: ${peso} kg\nAltura: ${altura} cm \nIMC: ${imc.toFixed(2)}\nResultado: Obesidade Grau II.`
      break
    case imc > 40.00:
      return `Peso: ${peso} kg\nAltura: ${altura} cm \nIMC: ${imc.toFixed(2)}\nResultado: Obesidade mórbida.`
      break

    default:
      return `Algo deu errado, não conseguimos calcular seu IMC.`
      break
  }
}

console.log(resultadoImc(9, 1.69))

# TODOS FUNÇÕES		: São blocos de código que podem ser reutilizados.
# print : Imprime dados na tela.

# TODOS MÉTODOS		: São funções que pertencem a uma classe. 
#       :

# TODOS MÓDULOS		: São arquivos que podem ser importados.
#       :

# TODOS BIBLIOTECAS	: São conjuntos de módulos que são disponibilizados 
#       :
