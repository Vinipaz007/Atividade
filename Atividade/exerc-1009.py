if __name__ == '__main__':
    nome = str(input('Digite seu nome:'))
    salario = float(input('Digite seu salário fixo:'))
    vendas = float(input('Digite o valor de vendas efetuadas no mês:'))
    porcentagem_das_vendas = vendas * 0.15
    salario_final = porcentagem_das_vendas + salario
    print(salario_final)