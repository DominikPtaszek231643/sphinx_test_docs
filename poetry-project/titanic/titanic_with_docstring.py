from pathlib import Path

import pandas as pd


def read_file(path: str or Path) -> pd.DataFrame:
    """
    Function which read path to Pandas DataFrame and imports it

    Args:
        path (str or Path): path to dataframe

    Returns:
        pd.DataFrame: Return imported dataframe

    """
    return pd.read_csv(path)


PATH = "data/titanic.csv"
titanic_df = read_file(PATH)

print(titanic_df)
