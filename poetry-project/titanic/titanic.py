import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/titanic.csv')

## Let's check if data has any missing values

print('Sum of missing values: ', df.isna().sum().sum())

### make a df.plot with no shared axis

# print(df.info())

df.hist(layout=(2, 3), figsize=(10, 20), sharex=False, sharey=False)

plt.show()

### Due to uneven distribution of Pclass, let's convert that to either low class or high


df['Pclass'] = df['Pclass'].apply(lambda x: 1 if x == 3 else 0)

print(df['Pclass'].value_counts())

print(df['Siblings/Spouses Aboard'].value_counts())
# Let's change Sibligns/Spouse Aboard to be either 0 or 1 and more due to skewed distribution

df['Siblings/Spouses Aboard'] = df['Siblings/Spouses Aboard'].apply(lambda row: 0 if row == 0 else 1)

print(df['Parents/Children Aboard'].value_counts())
# Let's change Parents/Children Aboard to be either 0 or 1 and more due to skewed distribution

df['Parents/Children Aboard'] = df['Parents/Children Aboard'].apply(lambda row: 0 if row == 0 else 1)

## Let's change sex to a binary equivalent


df['Sex'] = df['Sex'].apply(lambda row: 0 if row == 'female' else 1)

## Let's drop unrelevant columns

df = df.drop(columns=['Name'])

df.hist(layout=(3, 3), figsize=(10, 20), sharex=False, sharey=False)

plt.show()

x = df.drop(columns=['Survived'], axis=1)

print(x.columns)

y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
## Let's create simple Logistic Regression Model


log_reg = LogisticRegression(random_state=42)

log_reg.fit(X_train, y_train)

score = log_reg.score(X_test, y_test)

print('Score of basic model training :', score)
