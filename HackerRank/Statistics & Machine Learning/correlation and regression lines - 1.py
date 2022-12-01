import math as m

# Define functions
def mean(data):
    return sum(data) / len(data)

def var(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + (data[i] - mean(data)) ** 2
    return sum

def cov(data1, data2):
    sum = 0
    for i in range(len(data1)):
        sum += (data1[i] - mean(data1)) * (data2[i] - mean(data2))
    return sum

# Set data
physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

mean_physics = mean(physics)
mean_history = mean(history)

var_physics = var(physics)
var_history = var(history)

cov = cov(physics, history)
std = m.sqrt(var_physics * var_history)

# Correlation
r = cov / std
print(round(r, 3))