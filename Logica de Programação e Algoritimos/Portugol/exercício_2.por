programa {
  funcao inicio() {
    inteiro idade 

    escreva("digite sua idade: ")
    leia(idade)

    se(idade >= 0 e idade<=12 ){
    escreva("você é uma criança! ")
    }

    senao se(idade >=13 e idade<=17 ){
    escreva("você é uma adolecente! ")
    }

    senao se(idade >=18 e idade<=59 ){
    escreva("você é uma adulto! ")
    }

    senao se(idade >= 60  ){
    escreva("você é um idoso! ")

    }



    
  }
}
