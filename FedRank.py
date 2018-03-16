"""
The class will make classification of spatial clusters according to the some rule. Pondering of the structure is still
still in progress. s
"""

class FedRank():

    def __init__(self):
        pass

    def fit(self, X, y):
        '''

        :param X: input dataset
        :param y: rank
        :return:
        '''

    def predict(self, X):
        '''
        Return ranks for X input dataframe
        :param X: input pandas DataFrame
        :return:
        '''

        pass

    def transform(self, X, features =[], group_field = 'customer_id'):
        '''
        Add
        :param X: input Pandas DataFrame
        :param features: list of numerical feature to rank and transform
        :return:
        '''
        X_group = X.groupby(group_field)
        rename_dict = {col: col + '_rank' for col in features}
        c = X_group[features].transform(lambda x: x.rank()).astype(int).rename(columns=rename_dict)
        return X.merge(c, left_index=True, right_index=True, how='left')