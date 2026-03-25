"""
from scipy import optimize

def f(x):  # The rosenbrock function
    return .5 * (1 - x[0]) ** 2 + (x[1] - x[0] ** 2) ** 2


print(f([1, 1]))

print(optimize.differential_evolution(f, ((-5, 5), (-5, 5))))

result = optimize.brute(f, ((-5, 5), (-5, 5)))
print(result)

"""
"""
import numpy as np
from scipy.misc import electrocardiogram

ecg = electrocardiogram()
print(ecg)
print(ecg.shape, ecg.mean(), ecg.std())

import matplotlib.pyplot as plt

fs = 360
time = np.arrange(ecg.size) / fs
plt.plot(time, ecg)
plt.xlabel("time in s")
plt.ylabel("ECG in mV")
plt.xlim(9, 10.2)
plt.ylim(-1, 1.5)
plt.show()
"""
"""
import numpy as np
import math
import matplotlib.pyplot as plt
def f(x):
    return np.sin(x/5)*np.exp(x/10)+5*np.exp(-x/2)
x=np.linspace(0,16,150)
y=f(x)
plt.plot(x,y,color='r')
plt.show()
a1=0
a2=16
b1=f(a1)
b2=f(a2)
print(a1,b1)
print(a2,b2)
a=np.array([[1,a1],[1,a2]])
b=np.array([b1,b2])
w0,w1=np.linalg.solve(a,b)
y1=w0+w1*x

plt.plot(x,y,color='r')
plt.plot(x,y1,color='b')
plt.scatter([a1,a2],[b1,b2],color='g')
plt.show()


def get_error(y, y_pred):
    n = y.shape[0]
    sum_sqr = sum((y - y_pred) ** 2)
    mse = sum_sqr / n
    return mse
mse1 = get_error(y, y1)
print('Error = ', mse1)
a1 = 0
a2 = 4
a3 = 16
b1 = f(a1)
b2 = f(a2)
b3 = f(a3)
print(a1, b1)
print(a2, b2)
print(a3, b3)
a=np.array([[1,a1,a1**2],[1,a2,a2**2],[1,a3,a3**2]])
b=np.array([b1,b2,b3])
w0,w1,w2=np.linalg.solve(a,b)
y2=w0+w1*x+w2*x**2
plt.plot(x,y,color='r')
plt.plot(x,y2,color='b')
plt.scatter([a1,a2,a3],[b1,b2,b3],color='g')
plt.show()
a1 = 0
a2 = 4
a3 = 16
a4=16
b1 = f(a1)
b2 = f(a2)
b3 = f(a3)
b4=f(a4)
print(a1, b1)
print(a2, b2)
print(a3, b3)
print(a4,b4)
a=np.array([[1,a1,a1**2,a1**3],[1,a2,a2**2,a2**3],[1,a3,a3**2,a3**3],[1,a4,a4**2,a4**3]])
b=np.array([b1,b2,b3,b4])
w0,w1,w2,w3=np.linalg.solve(a,b)
y2=w0+w1*x+w2*x**2+w3*x**3
plt.plot(x,y,color='r')
plt.plot(x,y2,color='b')
plt.scatter([a1,a2,a3,a4],[b1,b2,b3,b4],color='b')
plt.show()
mse3=get_error(y,y2)
print('Error = ', mse3)
"""



