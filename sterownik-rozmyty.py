import numpy as np
import matplotlib.pyplot as plt

x_min, x_max, x_zasieg = -100, 100, 200
y_min, y_max, y_zasieg = -100, 0, 100
rampa_lewy, rampa_prawy, rampa_dol, rampa_gora = -30, 30, -10, 0
rampa_kat_docelowy_min = -20
rampa_kat_docelowy_max = 20
obrot_min, obrot_max = -20, 20
kat_min, kat_max = -180, 180
kat_zasieg = 360
ruch_skok = 5


def skret_prawo(kat):
    return np.exp(-((kat-90)/50)**2)


def lewa_czesc(x):
    return np.exp(-((x+np.abs(x_min+rampa_lewy)/2)/30)**2)


def prawa_czesc(x):
    return np.exp(-((x-np.abs(x_max+rampa_prawy)/2)/30)**2)


def srodek(x):
    return np.exp(-((x)/30)**2)


def skret_lewo(kat):
    return np.exp(-((kat + 90) / 50) ** 2)


def skret_srodek(x):
    return np.exp(-((x)/50)**2)


def gora(y):
    return np.exp(-((y + np.abs(y_max + y_min)/4) / 30) ** 2)


def dol(y):
    return np.exp(-((y + np.abs(y_max + y_min)/4*3) / 30) ** 2)


def get_skret(x1, y, kat):
    skret = (
            lewa_czesc(x1) * skret_prawo(kat) * gora(y) * 4
            + lewa_czesc(x1) * skret_srodek(kat) * 20
            + lewa_czesc(x1) * skret_prawo(kat) * dol(y) * 0
            + srodek(x1) * skret_srodek(kat) * 0
            + srodek(x1) * skret_prawo(kat) * (-20)
            + srodek(x1) * skret_lewo(kat) * 20
            + prawa_czesc(x1) * skret_srodek(kat) * (-20)
            + prawa_czesc(x1) * skret_lewo(kat) * gora(y) * (-4)
            + prawa_czesc(x1) * skret_lewo(kat) * dol(y) * 0
    ) / (
            lewa_czesc(x1) * skret_prawo(kat) * gora(y)
            + lewa_czesc(x1) * skret_srodek(kat)
            + lewa_czesc(x1) * skret_prawo(kat) * dol(y)
            + srodek(x1) * skret_srodek(kat)
            + srodek(x1) * skret_prawo(kat)
            + srodek(x1) * skret_lewo(kat)
            + prawa_czesc(x1) * skret_srodek(kat)
            + prawa_czesc(x1) * skret_lewo(kat) * gora(y)
            + prawa_czesc(x1) * skret_lewo(kat) * dol(y)
    )
    return skret


class PojazdPolozenie:
    def __init__(self, x, y, kat):
        self.x = x
        self.y = y
        self.kat = kat
        plt.scatter(x, y, marker='D')

    def zwroc_obrot(self):
        obrot = get_skret(self.x, self.y, self.kat)
        self.kat += obrot

    def ruch(self):
        self.x += (ruch_skok * np.sin(np.radians(self.kat / np.pi)*np.pi))
        self.y += (ruch_skok * np.cos(np.radians(self.kat / np.pi)*np.pi))
        plt.scatter(self.x, self.y, marker='D')

    # -1 = lose; 1 = win; 0 = play
    def check_status(self):
        if x_min <= self.x <= x_max:
            if y_min <= self.y <= y_max:
                if rampa_lewy <= self.x <= rampa_prawy and rampa_dol <= self.y <= rampa_gora and rampa_kat_docelowy_min <= self.kat <= rampa_kat_docelowy_max:
                    return 1
                return 0
        return -1


def show_map():
    plt.plot(
        [rampa_lewy, rampa_prawy, rampa_prawy, rampa_lewy, rampa_lewy],
        [rampa_gora, rampa_gora, rampa_dol, rampa_dol, rampa_gora],
        linestyle='dotted',
        color='r',
    )
    ax = plt.gca()
    ax.set_ylim([-100, 0])
    ax.set_xlim([-100, 100])
    plt.grid()
    plt.show()


def test():
    pojazd = PojazdPolozenie(-90, -10, 90)
    while pojazd.check_status() == 0:
        pojazd.zwroc_obrot()
        pojazd.ruch()
    wynik = 'zwycięstwo' if pojazd.check_status() == 1 else 'porażka'
    print(wynik)
    show_map()


test()
