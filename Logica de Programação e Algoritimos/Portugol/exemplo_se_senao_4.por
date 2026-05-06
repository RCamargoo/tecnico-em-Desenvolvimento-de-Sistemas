programa {
  funcao inicio() {
    cadeia operacao
    inteiro numero1, numero2
    real resultado

    escreva("digite a operação (+,-,*,/): ")
    leia(operacao)

    escreva("digite o primero numero: ")
    leia(numero1)
    
    escreva("digite o primeiro numero: ")
    leia(numero2)

    se(operacao == "+"){
      resultado = numero1 + numero2
    }
    senao se (operacao == "-"){
      resultado = numero1 - numero2
    }
    senao se (operacao == "*"){
      resultado = numero1 * numero2
    }
    senao se (operacao == "/"){
      resultado = numero1 / numero2
    }
    senao{
      escreva("operação ivalida")
    }
    escreva("o resultado é: ",resultado)

  }
}
