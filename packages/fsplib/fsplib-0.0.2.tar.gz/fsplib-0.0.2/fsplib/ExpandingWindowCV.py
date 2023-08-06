import numpy as np


class ExpandingWindowCV():
    """_summary_
    """

    def __init__(self, train_size: int = 2, test_size: int = 1) -> None:
        """_summary_

        Parameters
        ----------
        train_size : int
            Initial size of training set
        test_size : int
            Size of validation set
        """
        self.train_size = train_size
        self.test_size = test_size

    def split(self, X, y=None, groups=None):
        """_summary_
        """
        for i in range(12, 34 - self.train_size - self.test_size - 1):
            train = np.arange(i + self.train_size)
            test = np.arange(i + self.train_size, i + self.train_size + self.test_size)

            train_idx = X[X['date_block_num'].isin(train)].index
            test_idx = X[X['date_block_num'].isin(test)].index

            yield train_idx, test_idx



