import random
import numpy as np
import copy
import matplotlib.pyplot as plt

_X, _Y = np.meshgrid(np.linspace(0, 100, 100), np.linspace(0, 100, 100))
_Z = np.sin(_X * 0.05) + np.sin(_Y * 0.05) + 0.4 * np.sin(_X * 0.15) * np.sin(_Y * 0.15)


def euc_distance2d(p1, p2):
    return np.sqrt(pow(p2[0]-p1[0], 2)+pow(p2[1]-p1[1], 2))


def funkcja_przystosowania(x):
    return np.sin(x[0]*0.05)+np.sin(x[1]*0.05)+0.4*np.sin(x[0]*0.15)*np.sin(x[1]*0.15)


def firefly(N, beta_0, gamma, mu, iteracje_liczba):
    X = np.array([[random.uniform(0, 100), random.uniform(0, 100)] for x in range(N)])
    for x in range(iteracje_liczba):
        if x == 0:
            figure, axis = plt.subplots(1, 2)
            figure.suptitle('firefly')
            axis[0].contour(_X, _Y, _Z, levels=13)
            axis[0].set_title(f'początek\n'
                              f'najlepszy wynik to: {max([funkcja_przystosowania(z) for z in X])}')
            axis[0].scatter([z[0] for z in X], [z[1] for z in X], marker='*')
        for ida, a in enumerate(X):
            for idb, b in enumerate(X):
                if funkcja_przystosowania(b) > funkcja_przystosowania(a):
                    beta = beta_0 * np.exp(-gamma*pow(euc_distance2d(a, b), 2))
                    X[ida] = X[ida] + beta * (X[idb] - X[ida])
            X[ida] = X[ida] + np.array([random.uniform(-(100 * mu), 100 * mu), random.uniform(-(100 * mu), 100 * mu)])
            check_range(X[ida])
    axis[1].contour(_X, _Y, _Z, levels=13)
    axis[1].set_title(f'iteracja {iteracje_liczba}\n'
                      f'najlepszy wynik to: {max([funkcja_przystosowania(z) for z in X])}')
    axis[1].scatter([z[0] for z in X], [z[1] for z in X], marker='*', label='fireflies')
    plt.legend(loc='upper right')
    plt.show()


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
    firefly(40, 0.3, 0.1, 0.005, 100)


test()

