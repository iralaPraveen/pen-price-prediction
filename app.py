from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('pen_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    num_pens = int(request.form['pens'])
    if num_pens < 0:
        return render_template('index.html', prediction_text="Please enter a valid number of pens.")
    prediction = model.predict(np.array([[num_pens]]))[0]
    return render_template('index.html', prediction_text=f"Predicted Price: ₹{prediction:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
