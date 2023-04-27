if __name__ == '__main__':
    raio = float(input('Digite o valor do raio para saber o volume da esfera:'))
    pi = 3.14159
    volume = (4 / 3) * pi * (raio * raio* raio)
    print('O volume da esfera é: {:.3f}'.format(volume))