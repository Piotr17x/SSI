import random
import numpy as np
import copy
import matplotlib.pyplot as plt

X, Y = np.meshgrid(np.linspace(0, 100, 100), np.linspace(0, 100, 100))
Z = np.sin(X * 0.05) + np.sin(Y * 0.05) + 0.4 * np.sin(X * 0.15) * np.sin(Y * 0.15)


def funkcja_przystosowania(x):
    return np.sin(x[0]*0.05)+np.sin(x[1]*0.05)+0.4*np.sin(x[0]*0.15)*np.sin(x[1]*0.15)


def my_lambda(my, lmbd, turniej_rozmiar, mutacja_poziom, iteracje_liczba):
    rodz = []
    for x in range(my):
        rodz.append([random.uniform(0, 100), random.uniform(0, 100)])
    for x in range(iteracje_liczba):
        pot = []
        while len(pot) < lmbd:
            oss_turniej = [random.sample(copy.deepcopy(rodz), turniej_rozmiar)][0]
            os_n = max(oss_turniej, key=lambda z: funkcja_przystosowania(z))
            os_n[0] += random.uniform(-mutacja_poziom, mutacja_poziom)
            os_n[1] += random.uniform(-mutacja_poziom, mutacja_poziom)
            check_range(os_n)
            pot.append(os_n)
        if x == 0:
            figure, axis = plt.subplots(1, 2)
            figure.suptitle('µ + lambda')
            axis[0].contour(X, Y, Z, levels=13)
            axis[0].set_title(f'początek\n'
                              f'najlepszy wynik to: {max([funkcja_przystosowania(z) for z in rodz+pot])}')
            axis[0].scatter([x[0] for x in rodz], [x[1] for x in rodz], marker='*')
            axis[0].scatter([x[0] for x in pot], [x[1] for x in pot], marker='o')
        if x == iteracje_liczba-1:
            axis[1].contour(X, Y, Z, levels=13)
            axis[1].set_title(f'iteracja {iteracje_liczba}\n'
                              f'najlepszy wynik to: {max([funkcja_przystosowania(z) for z in rodz + pot])}')
            axis[1].scatter([x[0] for x in rodz], [x[1] for x in rodz], marker='*', label='pula rodz.')
            axis[1].scatter([x[0] for x in pot], [x[1] for x in pot], marker='o', label='pula pot.')
            plt.legend(loc='upper right')
            plt.show()
        rodz = sorted(rodz+pot, key=lambda z: funkcja_przystosowania(z), reverse=True)
        rodz = rodz[:my]


def check_range(os):
    if os[0] < 0:
        os[0] = 0
    elif os[0] > 100:
        os[0] = 100
    if os[1] < 0:
        os[1] = 0
    elif os[1] > 100:
        os[1] = 100


def test():
    my_lambda(4, 10, 2, 10, 20)


test()
