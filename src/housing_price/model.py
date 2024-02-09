# src/model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_model(data_file):
    # Load the dataset
    data = pd.read_csv(data_file)

    # Split the data into features and target
    X = data.drop('Price', axis=1)
    y = data['Price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model
