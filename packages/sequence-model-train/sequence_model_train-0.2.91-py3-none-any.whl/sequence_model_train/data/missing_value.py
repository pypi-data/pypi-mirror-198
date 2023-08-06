from sklearn.base import BaseEstimator, TransformerMixin


class FillNaRollMean(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns
        self.roll_mean = {}

    def fit(self, X, y=None):
        if self.columns is None:
            self.columns = X.columns.values
        for col_name in self.columns:
            self.roll_mean[col_name] = X[col_name].rolling(
                window=5,
                min_periods=1
            ).mean()
        return self

    def transform(self, X):
        for col_name, roll in self.roll_mean.items():
            X[col_name] = X[col_name].fillna(roll)
        return X


class DropNa(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.X = None

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.dropna()
        return X


class FillNaLastRow(BaseEstimator, TransformerMixin):
    def __call__(self):
        self.X = None

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X.fillna(method='ffill', inplace=True)
        X.fillna(value=0, inplace=True)
        return X
