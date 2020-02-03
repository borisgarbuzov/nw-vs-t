from os.path import dirname
import os
import pandas as pd


def read_matrix(name: str, index_col=None) -> pd.DataFrame:
    """
    Standard reading actions for matrix. 
    :param name: name of CSV file to be read. 
    :param index_col: a column name that should be made row names. 
    :return: matrix that was read. 
    """
    parent_dir = dirname(dirname(__file__))
    data_folder = os.path.join(parent_dir, "data")

    # read csv
    native_matrix_csv = name
    native_matrix = pd.read_csv(
        os.path.join(data_folder, native_matrix_csv),
        index_col=index_col)

    return native_matrix
