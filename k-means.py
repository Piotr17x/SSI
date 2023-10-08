from odczyt import FileReader
import numpy as np
import matplotlib.pyplot as plt

colors = ['r', 'b', 'g', 'y']


def euc_distance2d(p1, p2):
    return np.sqrt(pow(p2.x-p1.x, 2)+pow(p2.y-p1.y, 2))


def plot_k_means(V, df, axis):
    for idm, m in V.iterrows():
        axis.scatter(
            [df.loc[df['group'] == idm]['x']],
            [df.loc[df['group'] == idm]['y']],
            color=colors[idm],
        )
        axis.scatter(
            m['x'],
            m['y'],
            color=colors[idm],
            marker='D',
            edgecolors='#000000'
        )


def k_means(m: int, iters: int, df):
    V = df.sample(m)
    V = V.reset_index()
    df['group'] = -1
    for x in range(iters):
        for ids, s in df.iterrows():
            dist = np.inf
            for idm, m in V.iterrows():
                if dist > euc_distance2d(s, m):
                    dist = euc_distance2d(s, m)
                    df.loc[ids, 'group'] = idm

        if x == 0:
            figure, axis = plt.subplots(1, 2)
            figure.suptitle('Rozmieszczenie')
            axis[0].set_title('początek')
            plot_k_means(V, df, axis[0])

        for idm, m in V.iterrows():
            group = df.loc[df['group'] == idm]
            if len(group.index):
                V.loc[idm, 'x'] = group['x'].mean()
                V.loc[idm, 'y'] = group['y'].mean()

    axis[1].set_title(f'iteracja {iters}')
    plot_k_means(V, df, axis[1])
    plt.show()


def test_k_means():
    reader = FileReader('spirala.txt', ['x', 'y'], '\s+')
    return k_means(4, 10, reader.get_df())


test_k_means()
