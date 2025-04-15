import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Sample data: Number of pens vs price
# Assume price = 10 per pen
X = np.array([[1], [2], [3], [4], [5]])   # Number of pens
y = np.array([10, 20, 30, 40, 50])       # Price

model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'pen_price_model.pkl')
