import numpy as np


baza_wzor = [
    np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    np.array([[0, 1, 1, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]),
    np.array([[1, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 0]]),
]

baza_test = [
    np.array([[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]),
    np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]]),
    np.array([[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]]),
]


def euc_distance2d(p1, p2):
    return np.sqrt(pow(p2[0]-p1[0], 2)+pow(p2[1]-p1[1], 2))


def dopasuj(test_znak, baza_wzor):
    if not len(baza_wzor):
        print('brak znaków w bazie wzorcowej')
        return
    miara = -np.inf
    wynik = 0
    for idb, znak in enumerate(baza_wzor):
        miara_p_obustronna = -(miara_niepodobieństwa(test_znak, znak) + miara_niepodobieństwa(znak, test_znak))
        if miara_p_obustronna > miara:
            miara = miara_p_obustronna
            wynik = idb
    return wynik


def miara_niepodobieństwa(b1, b2):
    miara = 0
    for idr, row in enumerate(b1):
        for idc, point in enumerate(row):
            if point:
                odl_min = np.inf
                for idr_2, row2 in enumerate(b2):
                    for idc_2, point2 in enumerate(row2):
                        if point2:
                            odl_min = min(
                                odl_min,
                                euc_distance2d(
                                    (idr, idc),
                                    (idr_2, idc_2),
                                )
                            )
                miara += odl_min
    return miara


def test_dopasuj():
    wynik = dopasuj(baza_test[1], baza_wzor)
    print(f'Znak testowy jest najbardziej podobny'
          f' do znaku wzorcowego z numerem {wynik+1}')


test_dopasuj()
