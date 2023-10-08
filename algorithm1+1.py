import numpy as np
import random
import matplotlib.pyplot as plt


def funkcja_przystosowania(x):
    return np.sin(x/10)*np.sin(x/200)


def alg_1plus1(rozrzut, wsp_przyrostu, l_iteracji, zakres_zmiennosci=(0, 100)):
    x = random.uniform(zakres_zmiennosci[0], zakres_zmiennosci[1])
    y = funkcja_przystosowania(x)
    for i in range(l_iteracji):
        x_pot = x + random.uniform(-rozrzut, rozrzut)
        if x_pot > zakres_zmiennosci[1]:
            x_pot = zakres_zmiennosci[1]
        elif x_pot < zakres_zmiennosci[0]:
            x_pot = zakres_zmiennosci
        y_pot = funkcja_przystosowania(x_pot)
        if y_pot >= y:
            x = x_pot
            y = y_pot
            rozrzut *= wsp_przyrostu
        else:
            rozrzut /= wsp_przyrostu
        print(f'Iteracja #{i+1}\n'
              f'x = {x}\n'
              f'y = {y}\n'
              f'rozrzut = {rozrzut}\n'
              f'+=+=+=+=+=+')
        plt.title('Algorytm 1+1')
        plt.plot(x, y, marker='o', color='b')
    x = np.arange(0, 100, 0.5)
    plt.plot(x, funkcja_przystosowania(x))
    plt.show()


alg_1plus1(10, 1.1, 100)
