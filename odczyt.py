import pandas as pd


class FileReader:
    def __init__(self, path: str, header: list, sep: str = '\t'):
        self.path = path
        try:
            self.df = pd.read_csv(
                self.path,
                header=None,
                sep=sep,
                names=header
            )
        except FileNotFoundError:
            print('Niepoprawna nazwa pliku')

    def get_df(self) -> pd.core.frame.DataFrame:
        return self.df

    def get_row(self, row_numb: int) -> pd.core.series.Series:
        return self.df.iloc[row_numb]


def test():
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
    iris = reader.get_df()
    print(iris)
    print(iris.sepal_width_in_cm)
    print(reader.get_row(3))


# test()
