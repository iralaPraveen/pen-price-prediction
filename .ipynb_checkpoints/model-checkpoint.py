import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import joblib

# Sample data: Number of pens vs price
# Assume price = 10 per pen
X = np.array([[1], [2], [3], [4], [5]])   # Number of pens
y = np.array([10, 20, 30, 40, 50])  

df = pd.DataFrame({
    'Number_of_Pens': X.flatten(),
    'Price': y      
})
print("Basic Informatin")
print(df.info())  

print("Basic Statistics")
print(df.describe())

#visulization


#SCatter plot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='Number_of_Pens', y='Price', data=df, ci=None, line_kws={"color": "red"})
plt.title("Number of Pens vs Price")
plt.xlabel("Number of Pens")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
plt.show()

#Correlation heatmap
plt.figure(figsize=(4, 3))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()


model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'pen_price_model.pkl')


