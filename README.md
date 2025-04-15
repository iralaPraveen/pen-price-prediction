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

Using `LinearRegression` from `scikit-learn`, the model learns the formula:

