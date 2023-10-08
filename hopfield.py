import numpy as np

baza_wzor = [
    np.array([[1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1]]),
    np.array([[1, -1, -1, -1, 1], [-1, 1, -1, 1, -1], [-1, -1, 1, -1, -1], [-1, 1, -1, 1, -1], [1, -1, -1, -1, 1]]),
    np.array([[-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1], [1, 1, 1, 1, 1], [-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1]]),
]

baza_test = [
    np.array([[-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1], [-1, 1, -1, -1, -1]]),
    np.array([[1, 1, -1, -1, 1], [-1, 1, -1, 1, -1], [-1, 1, 1, 1, -1], [-1, 1, -1, 1, -1], [1, 1, -1, -1, 1]]),
    np.array([[-1, -1, -1, -1, -1], [-1, -1, 1, -1, -1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1], [-1, -1, 1, -1, -1]]),
    np.array([[-1, 1, 1, 1, 1], [1, -1, 1, 1, 1], [1, -1, 1, 1, 1], [1, -1, 1, 1, 1], [1, -1, 1, 1, 1]]),
]


class Hopfield:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.n = h * w
        self.weights = np.zeros((self.n, self.n))

    def naucz_obraz(self, wzor):
        flat = wzor.flatten()
        for i in range(self.n):
            for j in range(self.n):
                if j == i:
                    continue
                self.weights[i][j] += (flat[i]*flat[j])/self.n

    def rozpoznaj_obraz(self, obraz):
        flat = obraz.flatten()
        for i in range(self.n):
            suma = 0
            for j in range(self.n):
                if i == j:
                    continue
                suma += flat[j]*self.weights[i][j]
            flat[i] = 1 if suma >= 0 else -1
        rozp_obraz = np.resize(flat, (self.h, self.w))
        if np.array_equal(rozp_obraz, obraz):
            return False
        return rozp_obraz


def test_hopfield():
    hopfield = Hopfield(5, 5)
    for wzor in baza_wzor:
        hopfield.naucz_obraz(wzor)
    print(hopfield.rozpoznaj_obraz(baza_test[1]))


test_hopfield()
