# src/train.py

from housing_price.model import train_model
import joblib

if __name__ == '__main__':
    data_file = 'data/housing.csv'
    model = train_model(data_file)

    # Save the trained model to a file
    joblib.dump(model, 'house_price_model.pkl')
