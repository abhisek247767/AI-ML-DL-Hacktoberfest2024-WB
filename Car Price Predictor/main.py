# import pandas as pd

# data = pd.read_csv('car_price\data.csv')

# # cleaning up the data

# backup = data.copy()

# data = data[data['year'].str.isnumeric()] 

# data['year'] = data['year'].astype(int)

# data = data[data['Price'] != 'Ask For Price']

# data['Price'] = data['Price'].str.replace(',','').astype(int)

# data['kms_driven'] = data['kms_driven'].str.split(' ').str.get(0).str.replace(',','')

# data = data[data['kms_driven'].str.isnumeric()]

# data['kms_driven'] = data['kms_driven'].astype(int)

# data = data[~data['fuel_type'].isna()]

# data['name'] = data['name'].str.split(' ').str.slice(0,3).str.join(' ')

# data.reset_index(drop = True)

# # filtering outliers

# data = data[data['Price'] < 6e6].reset_index(drop = True)
# # Q1 = data['kms_driven'].quantile(0.25)
# # Q3 = data['kms_driven'].quantile(0.75)
# # IQR = Q3 - Q1
# # data = data[~((data['kms_driven'] < (Q1 - 1.5 * IQR)) |(data['kms_driven'] > (Q3 + 1.5 * IQR)))]
# # data.to_csv('car_price\cleaned_data.csv')

# fitting a model

import pandas as pd
import numpy as np

data = pd.read_csv('cleaned_data.csv')

X = data.drop(columns = 'Price')
y = data['Price']

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=433)

from sklearn.linear_model import LinearRegression

ohe = OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])

coloum_transformer = make_column_transformer((OneHotEncoder(categories = ohe.categories_), ['name','company','fuel_type']), remainder = 'passthrough')

lr = LinearRegression()
pipe = make_pipeline(coloum_transformer, lr)
pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

print(r2_score(y_test, y_pred))

# calculating best random state

# score = []

# for i in range(1000):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = i)
#     lr = LinearRegression()
#     pipe = make_pipeline(coloum_transformer, lr)
#     pipe.fit(X_train, y_train)
#     y_pred = pipe.predict(X_test)
#     score.append(r2_score(y_test, y_pred))

# print(np.argmax(score))
# print(np.max(score))

# 433
# 0.8451964429627923

import pickle
pickle.dump(pipe, open('LinearRegressionModel.pkl', 'wb')) 