from odczyt import FileReader
import numpy as np
import matplotlib.pyplot as plt
import random

colors = ['r', 'g', 'b']


class FCM:
    def __init__(self, df, c_numb, m=2):
        self.m = m
        self.c_numb = c_numb
        self.df = df
        self.V = df.sample(c_numb)
        self.V = self.V.reset_index()

        for group in range(c_numb):
            self.df[f'U_{group}'] = -1
            self.df[f'D_{group}'] = 0

        for ids, s in df.iterrows():
            r = [random.random() for group in range(c_numb)]
            for group in range(c_numb):
                df.loc[ids, f'U_{group}'] = r[group]/sum(r)

    def set_centroids(self):
        for idm in range(len(self.V.index)):
            u = sum([pow(self.df.iloc[ids][f'U_{idm}'], 2) for ids in range(len(self.df.index))])
            self.V.loc[idm, 'x'] = sum([pow(self.df.iloc[ids][f'U_{idm}'], 2)*self.df.iloc[ids]['x'] for ids in range(len(self.df.index))])/u
            self.V.loc[idm, 'y'] = sum([pow(self.df.iloc[ids][f'U_{idm}'], 2)*self.df.iloc[ids]['y'] for ids in range(len(self.df.index))])/u

    def update_membership(self):
        for ids in range(len(self.df.index)):
            for idm, m in self.V.iterrows():
                self.df.loc[ids, f'D_{idm}'] = self.euc_distance2d(self.df.iloc[ids], m) if self.euc_distance2d(self.df.iloc[ids], m) > 0.0005 else 0.0005
            for idm, m in self.V.iterrows():
                self.df.loc[ids, f'U_{idm}'] = pow(pow(sum([pow(self.df.iloc[ids][f'D_{idm}'], 2)/pow(self.df.iloc[ids][f'D_{group}'], 2) for group in range(self.c_numb)]), 1/(self.m-1)), -1)

    @staticmethod
    def euc_distance2d(p1, p2):
        return np.sqrt(pow(p2.x-p1.x, 2)+pow(p2.y-p1.y, 2))

    def iterate(self, x):
        for i in range(x):
            self.set_centroids()
            if i == 0 and self.c_numb == 3:
                figure, axis = plt.subplots(1, 2)
                figure.suptitle('Rozmieszczenie')
                axis[0].set_title('początek')
                plot_fcm(self.V, self.df, axis[0])
            self.update_membership()
        if self.c_numb == 3:
            axis[1].set_title(f'iteracja {x}')
            plot_fcm(self.V, self.df, axis[1])
            plt.show()


def plot_fcm(V, df, axis):
    for ids, s in df.iterrows():
        axis.scatter(
            s['x'],
            s['y'],
            color=(s['U_0'], s['U_1'], s['U_2'])
        )
    for idm, m in V.iterrows():
        axis.scatter(
            m['x'],
            m['y'],
            color=colors[idm],
            marker='D',
            edgecolors='#000000'
        )


def test_fcm():
    reader = FileReader('spirala.txt', ['x', 'y'], '\s+')
    fcm = FCM(reader.get_df(), 3)
    fcm.iterate(7)
    return fcm.df


test_fcm()
