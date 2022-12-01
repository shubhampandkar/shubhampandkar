from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
f, n = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(n):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < f:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set Polynomial Features
poly = PolynomialFeatures(degree=3)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(poly.fit_transform(np.array(X)), Y)

# Get the parameters X for discovery the Y
test_rows = int(input())
test_X = []
for i in range(test_rows):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    test_X.append(x)

# Gets the result and show on the screen
y_pred = model.predict(poly.fit_transform(np.array(test_X)))
for i in range(len(y_pred)):
    print(round(y_pred[i],2))

