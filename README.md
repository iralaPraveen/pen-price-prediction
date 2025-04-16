# Pen Price Predictor 

A simple linear regression model that predicts the total cost of pens based on the quantity. Built using Python, scikit-learn, Flask, and basic HTML/CSS.

---

## Overview 

This project demonstrates how machine learning can be applied to predict the price of pens using just **one feature** — the number of pens.

We assume each pen costs ₹10, and the model is trained on this linear relationship. It also includes a Flask web app for interacting with the model through a simple UI.

---

### How It Works 

The model is trained using the following logic:

| Number of Pens | Price (₹) |
|----------------|-----------|
| 1              | 10        |
| 2              | 20        |
| 3              | 30        |
| 4              | 40        |
| 5              | 50        |

Using `LinearRegression` from `scikit-learn`, the model learns the formula:price = 10 × number_of_pens


It is saved as `pen_price_model.pkl` using `joblib` and used in a Flask app (`app.py`) that takes input from the user and displays the predicted price.

---

#### Technologies Used 

- Python
- scikit-learn
- Flask
- HTML/CSS (for front-end)
- joblib

---


###### Smallest Header 

### 🚀 To Run the App Locally:

1. **Clone the repository:**
   ```bash
   git clone git@github.com:iralaPraveen/pen-price-prediction.git
   cd pen-price-prediction

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python app.py

Then visit http://127.0.0.1:5000 in your browser{you will see the app is running}




