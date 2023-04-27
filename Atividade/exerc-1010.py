if __name__ == '__main__':
    codigo1 = int(input('Digite o código da peça:'))
    numero1 = int(input('Digite o número de peças:'))
    valor1 = float(input('Digite o valor da peça:'))

    codigo2 = int(input('Digite o código da peça:'))
    numero2 = int(input('Digite o número de peças:'))
    valor2 = float(input('Digite o valor da peça:'))

    total = (numero1 * valor1) + (numero2 * valor2)

    print('O valor a pagar é: R$ {:.2f}'.format(total))