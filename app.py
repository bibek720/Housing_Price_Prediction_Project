from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load the trained model
model = joblib.load('house_price_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        # Get input features from the submitted form
        square_feet = float(request.form['square_feet'])
        num_bedrooms = int(request.form['num_bedrooms'])
        num_bathrooms = int(request.form['num_bathrooms'])
        num_floors = int(request.form['num_floors'])
        year_built = int(request.form['year_built'])

        # Make a prediction using the loaded model
        input_features = np.array([[square_feet, num_bedrooms, num_bathrooms, num_floors, year_built]])
        predicted_price = model.predict(input_features)[0]

        return f'Predicted Price: ${predicted_price:.2f}'

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
