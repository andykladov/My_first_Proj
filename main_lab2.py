"""
river = ['Амазонка', 'Лена', 'Иртыш', 'Обь']
print(river)
print(type(river))
print(len(river))
river[0] = 'Васюган'
print(river)
city = ('Moscow', 'Sochi', 'Penza')
print(city)
print(type(city))
city = list(city)
print(type(city))
river = tuple(river)
print(type(river))
print(city)
city.append('Sevastopol')
print(city)
city.insert(2, 'Pskov')
print(city)
if 'Moscow' in city:
    print('Moscow present')
else:
    print('Not present')
city.append('Moscow')
print(city)
n=city.count('Moscow')
print(n)

a=[1,3,5,8,4]
for i in a:
    print(i)

import random
def alpha():
    n=random.randint(1,100)
    return n
b=[]
for i in range(10):
    b.append(alpha())
    print(b)
"""
"""
a=range(10)
print(a)
print(type(a))
print(*a)
for i in a:
    print(i)
a=range(3,79,5)
print(*a)

a=list(a)
print(a)
"""
"""
a={1,1,1,2,2,3,5,8}
print(a)
print(type(a))
"""
"""
a={'Яблоки','Груши','Персики','Фйва'}
b={'Груши','Фйва','Персики','Tыква'}
print(a.union(b))
print(a.intersection(b))
"""
"""
countries = ['India', 'Brazil', 'China', 'Nigeria', 'Bangladesh', 'U.S.', 'Russia', 'Pakistan', 'Mexico']
populations = [1326801576, 209567920, 1382323332, 186987563, 162910864, 324118787, 143439832, 192826502, 128632004]
print(dict(zip(countries, populations)))

from operator import itemgetter
print(sorted(populations_by_countries.items(), key=itemgetter(1),reverse=True))
"""
"""
import numpy as np
a=[1,2,3,4,5,6]
b=np.array(a)
print(b)
print(type(b))

print(a*3)
print(b*3)
"""
"""
def f(x):
   y=x**2
   return y

print()
y=f(x)
print(y)

import matplotlib.pyplot as plt
plt.plot(x.y)
plt.show()
"""
"""
import numpy as np
x=np.linspace(-1,1,100)

a=-1
b=1
N=100
delta_x=(b-a)/N
integral=delta_x*sum(y)
print('Integral = ',integral)

"""


