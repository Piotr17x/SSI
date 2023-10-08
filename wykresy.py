from odczyt import FileReader
import matplotlib.pyplot as plt
import numpy as np


def clear_graph():
    plt.clf()


def draw_lines(x_values, y_values, line_style='solid', color='blue', label=''):
    if len(x_values) != len(y_values):
        print('Listy są różnej wielkości')
        return
    plt.plot(
        x_values,
        y_values,
        linestyle=line_style,
        color=color,
        label=label,
    )


def draw_points(x_values, y_values, marker='o', color='blue', label=''):
    if len(x_values) != len(y_values):
        print('Listy są różnej wielkości')
        return
    plt.scatter(
        x_values,
        y_values,
        marker=marker,
        color=color,
        label=label,
    )


def test():
    plt.title('Test')
    draw_lines([1, 2, 3, 4, 5], [1, 2, 3, 5, 4])
    clear_graph()
    draw_points([1, 2, 3, 5, 4], [1, 2, 3, 4, 5])
    plt.show()


# test()


def zadanie_3():
    plt.title('Wykres zadanie 3')
    draw_lines(
        [0, 0.8, 1.4, 1.8, 2, 1.8, 1.4, 0.8, 0, -0.8, -1.4, -1.8, -2, -1.8, -1.4, -0.8, 0],
        [2, 1.8, 1.4, 0.8, 0, -0.8, -1.4, -1.8, -2, -1.8, -1.4, -0.8, 0, 0.8, 1.4, 1.8, 2],
        color='red',
        label='łamane'
    )
    th = np.linspace(0, 2*np.pi, 100)
    draw_lines(1.8*np.cos(th), 1.8*np.sin(th), color='black', label='koło')
    draw_points([-1, 0, 1], [1, 0, 1], marker='D', label='punkty')
    th2 = np.linspace(np.pi, 2*np.pi, 100)
    draw_lines(
        np.arange(-1, 1, 0.02),
        np.sin(th2),
        color='yellow',
        label='sinus',
    )
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


# zadanie_3()


def zadanie_4():
    reader = FileReader(
        'iris.txt',
        [
            'sepal_length_in_cm',
            'sepal_width_in_cm',
            'petal_length_in_cm',
            'petal_width_in_cm',
            'class',
        ]
    )
    df = reader.get_df()
    class_1 = df.loc[df['class'] == 1]
    class_2 = df.loc[df['class'] == 2]
    class_3 = df.loc[df['class'] == 3]
    figure, axis = plt.subplots(2, 2)
    figure.suptitle('Iris based on classes.')

    axis[0, 0].scatter(class_1['petal_length_in_cm'], class_1['petal_width_in_cm'])
    axis[0, 0].scatter(class_2['petal_length_in_cm'], class_2['petal_width_in_cm'], color='r')
    axis[0, 0].scatter(class_3['petal_length_in_cm'], class_3['petal_width_in_cm'], color='g')
    axis[0, 0].set_xlabel('petal_length_in_cm')
    axis[0, 0].set_ylabel('petal_width_in_cm')

    leg_1 = axis[0, 1].scatter(class_1['sepal_width_in_cm'], class_1['petal_width_in_cm'])
    leg_2 = axis[0, 1].scatter(class_2['sepal_width_in_cm'], class_2['petal_width_in_cm'], color='r')
    leg_3 = axis[0, 1].scatter(class_3['sepal_width_in_cm'], class_3['petal_width_in_cm'], color='g')
    axis[0, 1].set_xlabel('sepal_width_in_cm')
    axis[0, 1].set_ylabel('petal_width_in_cm')

    axis[1, 0].scatter(class_1['sepal_length_in_cm'], class_1['petal_width_in_cm'])
    axis[1, 0].scatter(class_2['sepal_length_in_cm'], class_2['petal_width_in_cm'], color='r')
    axis[1, 0].scatter(class_3['sepal_length_in_cm'], class_3['petal_width_in_cm'], color='g')
    axis[1, 0].set_xlabel('sepal_length_in_cm')
    axis[1, 0].set_ylabel('petal_width_in_cm')

    axis[1, 1].scatter(class_1['sepal_width_in_cm'], class_1['petal_length_in_cm'])
    axis[1, 1].scatter(class_2['sepal_width_in_cm'], class_2['petal_length_in_cm'], color='r')
    axis[1, 1].scatter(class_3['sepal_width_in_cm'], class_3['petal_length_in_cm'], color='g')
    axis[1, 1].set_xlabel('sepal_width_in_cm')
    axis[1, 1].set_ylabel('petal_length_in_cm')
    plt.legend([leg_1, leg_2, leg_3], ["class 1", "class 2", "class 3"])

    plt.show()


# zadanie_4()
