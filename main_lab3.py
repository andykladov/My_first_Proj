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





