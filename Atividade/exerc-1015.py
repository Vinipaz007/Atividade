if __name__ == '__main__':

    p1 = input('Digite dois valores em sequência separando-os com um espaço : ').split()
    x1, y1 = float(p1[0]), float(p1[1])

    p2 = input('Digite outros dois valores em sequência separando-os com um espaço : ').split()
    x2, y2 = float(p2[0]), float(p2[1])

    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

    print('{:.4f}'.format(d))