a = 15 # walk to bus stop
b = 75 # bus journey
c = a + b # way by bus
d = 90 # car drive
e = 5 # walk from car
f = d + e # way by car
# Compare c to f. If the returned value is True, then we get the result.
# In this program, row 1 returns True, and hence c < f.  
print(c > f)
print(c < f)
# Bus is quicker. The time of way by car is longer.

X = 1 < 5
Y = 6 > 9
W = X and Y
print(X)
print(Y)
print(W) 
#X, Y, W
#True, True, True
#True, False, False
#False, True, False
#False, False, False
