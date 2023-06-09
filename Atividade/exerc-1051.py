if __name__ == '__main__':
    renda = float(input('Digite seu salário: '))

    faixas = [
        (0.0, 2000.0, 0.0),
        (2000.01, 3000.0, 0.08),
        (3000.01, 4500.0, 0.18),
        (4500.01, float("inf"), 0.28)
    ]

    imposto = 0.0
    for faixa in faixas:
        if renda > faixa[0]:
            if renda <= faixa[1]:
                imposto += (renda - faixa[0]) * faixa[2]
                break
            else:
                imposto += (faixa[1] - faixa[0]) * faixa[2]
                renda -= (faixa[1] - faixa[0])

    imposto = round(imposto, 2)

    if imposto == 0.0:
        print("Isento")
    else:
        print("R$ {:.2f}".format(imposto))
