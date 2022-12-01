import sys
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
# Set dataset to training
dataset = pd.read_csv('trainingdata.txt', header=None)
plt.plot(dataset.iloc[:,0], dataset.iloc[:,1], 'ro')
plt.ylabel('Laptop Battery Life')
plt.show()

# removing records with duration of time greater than 8
dataset = dataset[dataset.iloc[:,1] < 8]

# Add bias
dataset.insert(0, len(dataset.columns), 0)

# Separate variables (dependent and independent)
X = dataset.iloc[:,0:2].to_numpy()
Y = dataset.iloc[:,2].to_numpy()

# Create the classifier model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Set new value to predict
timeCharged = float(input().strip())
result = model.predict([[0, timeCharged]])
if result[0] > 8:
    print (8.0)
else:
    print (round(result[0],2))