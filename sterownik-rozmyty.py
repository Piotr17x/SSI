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


class PojazdPolozenie:
    def __init__(self, x, y, kat):
        self.x = x
        self.y = y
        self.kat = kat
        plt.scatter(x, y, marker='D')

    def get_turn(self, goal):
        goal = (goal + 360) % 360
        kat = (self.kat + 360) % 360
        if kat > 180 and goal == 0:
            goal = 360
        if goal < kat:
            ob = goal - kat
            return ob if ob >= obrot_min else obrot_min
        elif goal > kat:
            ob = goal - kat
            return ob if ob <= obrot_max else obrot_max
        return 0

    def zwroc_obrot(self):
        if self.x <= rampa_lewy:
            if self.y >= y_min/2:
                obrot = self.get_turn(135)
            else:
                obrot = self.get_turn(90)
        elif rampa_lewy < self.x <= rampa_prawy:
            obrot = self.get_turn(0)
        elif rampa_prawy < self.x:
            if self.y >= y_min/2:
                obrot = self.get_turn(-135)
            else:
                obrot = self.get_turn(-90)
        self.kat += obrot
        if self.kat < kat_min:
            self.kat += kat_zasieg
        elif self.kat > kat_max:
            self.kat -= kat_zasieg

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
