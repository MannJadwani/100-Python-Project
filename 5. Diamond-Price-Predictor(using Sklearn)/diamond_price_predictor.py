import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

diamond_prices=pd.read_csv("/content/sample_data/Diamonds-Prices2022.csv")

lm = LinearRegression()

x= diamond_prices[["carat"]]
y= diamond_prices[["price"]]

diamond_model=lm.fit(x,y)
diamond_prices.keys()

price=input("Enter the carat of the diamond you want to buy:")
X=diamond_model.predict([[price]])
print(X)

#this programm will require you to install sklearn,numpy and pandas to run it 