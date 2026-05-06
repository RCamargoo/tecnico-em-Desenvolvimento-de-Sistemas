programa {
  funcao inicio() {
    inteiro l1, l2, l3

    escreva("digite o lado 1: ")
    leia(l1)

    escreva("digite lado 2: ")
    leia(l2)

    escreva("digite lado 3: ")
    leia(l3)

    se (l1 == l2 e l1 == l3 e l2 == l3){
    escreva("triângulo equilátero")
    }

    senao se  (l1 == l2 ou l3 == l2 ou l1 == l3 ){
      escreva("triângulo isóceles")
    }

    senao se (l1 != l2 e l2 != l3 e l1!= l3){
      escreva("triangulo ecaleno")
    }

    









    
  }
}
