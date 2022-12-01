import numpy as np
import math as m
import statistics as stpy
from scipy import stats

# Input
total = int(input())
numbers = list(map(int, input().split()))

# Set statistics values
mean = np.mean(numbers)
median = np.median(numbers)
mode = int(stats.mode(numbers)[0])
stdev = stpy.pstdev(numbers)
confidence_interval = 1.96 * (stdev / m.sqrt(total))
min_confidence = round(mean - confidence_interval, 1)
max_confidence = round(mean + confidence_interval, 1)

# Show the final result
print(round(mean,1))
print(round(median,1))
print(mode)
print(round(stdev,1))
print("{} {}".format(min_confidence, max_confidence))