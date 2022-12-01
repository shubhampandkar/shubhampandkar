import math as m
slope_x = 9/20
slope_y = 4/5
var_x = 3
r = m.sqrt(slope_x * slope_y)

var_y = (r * (var_x/slope_x)) ** 2
print(round(var_y,1))
