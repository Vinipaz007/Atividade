if __name__ == '__main__':
    num = int(input('Digite seu número:'))
    hora_trabalhada = int(input('Digite a quantidade de horas trabalhada:'))
    valor_por_hr = float(input('Digite o valor que você recbe por hora:'))
    salario = hora_trabalhada * valor_por_hr
    print('NÚMERO:{}\nsalário: {}'.format(num, salario))