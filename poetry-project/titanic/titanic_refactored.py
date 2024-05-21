import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def read_file(path: str or Path) -> pd.DataFrame:
    return pd.read_csv(path)


PATH = "data/titanic.csv"
titanic_df = read_file(PATH)

print(titanic_df)


def check_missing_values_in_df(df: pd.DataFrame) -> None:
    total_missing_val_num = df.isna().sum().sum()

    if total_missing_val_num > 0:
        print(
            f"There are missing values in dataframe\nExact number: {total_missing_val_num}"
        )

    else:
        print("DataFrame does not contain any missing values!")


check_missing_values_in_df(titanic_df)


def plot_df_histogram(df: pd.DataFrame) -> None:
    layout_rows = math.ceil(df.shape[1] // 2)

    df.hist(layout=(layout_rows, 3), figsize=(10, 20), sharex=False, sharey=False)

    plt.show()


plot_df_histogram(titanic_df)


### Due to uneven distribution of Pclass, let's convert that to either low class or high


def transform_df_column_to_binary(
    df: pd.DataFrame, col_name: str, condition_func
) -> pd.Series:
    df = df.copy()
    df[col_name] = df[col_name].apply(condition_func)

    print(f"Column {col_name} after transormation:", df[col_name].value_counts())

    return df[col_name]


titanic_df["Pclass"] = transform_df_column_to_binary(
    titanic_df, "Pclass", lambda x: 1 if x == 3 else 0
)

# Let's change Sibligns/Spouse Aboard to be either 0 or 1 and more due to skewed distribution

titanic_df["Siblings/Spouses Aboard"] = transform_df_column_to_binary(
    titanic_df, "Siblings/Spouses Aboard", lambda row: 0 if row == 0 else 1
)

# Let's change Parents/Children Aboard to be either 0 or 1 and more due to skewed distribution


titanic_df["Parents/Children Aboard"] = transform_df_column_to_binary(
    titanic_df, "Parents/Children Aboard", lambda row: 0 if row == 0 else 1
)

titanic_df["Sex"] = transform_df_column_to_binary(
    titanic_df, "Sex", lambda row: 0 if row == "female" else 1
)


def drop_cols_from_df(df: pd.DataFrame, col_names: list[str]) -> pd.DataFrame:
    return df.drop(columns=col_names)


titanic_df = drop_cols_from_df(titanic_df, ["Name"])

plot_df_histogram(titanic_df)


def split_data_into_sets(
    df: pd.DataFrame, target_col_name: str
) -> [pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    x = drop_cols_from_df(df, [target_col_name])

    y = df[target_col_name]

    return train_test_split(x, y, test_size=0.3)


X_train, X_test, y_train, y_test = split_data_into_sets(titanic_df, "Survived")


def init_model(model_obj):
    return model_obj(random_state=42)


def train_model(model_obj, data: list):
    model_obj.fit(*data)


log_reg = init_model(LogisticRegression)

train_model(log_reg, data=[X_train, y_train])


def evaluate_model(model_obj, data: list):
    score = model_obj.score(*data)

    print("Score of basic model training :", score)


evaluate_model(log_reg, data=[X_test, y_test])
