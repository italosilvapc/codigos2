num1 = float(input('Digite o primeiro numero '))
operacao = input('Digite + para soma, - para subtração, * para multiplicação e / para divisão ')
num2 = float(input('Digite o segundo numero '))

match operacao:
    case '+':
        soma = num1 + num2
        print('a soma é ' , soma)
        

    case '-':
        subt = num1 - num2
        print('a subtração é ' , subt)
    

    case '*':
        mult = num1 * num2
        print('a multiplicação é ' , mult)
   

    case '/':
        div = num1 / num2
        print('a divisão é ' , div)
    case _:
        print('Opção inválida')