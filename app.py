from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("credit_card_fraud_model.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Take input values
        features = [float(x) for x in request.form.values()]

        # Convert to numpy array
        final_features = np.array(features).reshape(1, -1)

        # Predict
        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = "⚠ Fraudulent Transaction Detected"
        else:
            result = "✅ Legitimate Transaction"

        return render_template(
            'index.html',
            prediction_text=result
        )

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
