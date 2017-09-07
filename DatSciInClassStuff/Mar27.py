from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

xo = [151, 174, 138, 186, 128, 136, 179, 163, 152, 131]
yo = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

x = np.array(xo).reshape(-1, 1)
y = np.array(yo).reshape(-1, 1)

x_train = x[:-2]
y_train = y[:-2]

x_test = x[-2:]
y_test = y[-2:]

regr = linear_model.LinearRegression()

regr.fit(x_train, y_train)

print("Coefficients: " + str(regr.coef_))

pred = regr.predict(170)
print(pred)

plt.scatter(x, y, color="black")
plt.plot(x_test, regr.predict(x_test), color="blue", linewidth=3)
plt.show()
