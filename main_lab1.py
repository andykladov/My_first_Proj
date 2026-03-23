"""
print("Мир")
age=16
print('Привет! Мне',age,'лет')
print(type(age))
"
price=308.25 #Цена сыра
print('Сыр стоит ', price,'Рублей')
print(type(price))
MyName='Andy'
print(type(MyName))
print('Привет, я ', MyName)
"
age=input('How old are you')
print('I am ',age,'years old')
print(type(age))
age=int(age)
print(type(age))
"
price=input ('How much cost a cap of coffi')
print('Coffe cost',price,'roubl')
print(type(price))
price=float(price)
print(type(price))
"
a1='О сколько нам открытий чудных'
a2='\nГотовят просвященья дух'
a3='\nопыт, сын'
a4='\nИ гений парадоксов'
a=a1+a2+a3+a4
print(a)
myName='Andy'
age=17
s='Hello! My name is ' + myName +'I am' + str(age)+ 'years old'
print(s)

"
a1=-3
a2=16
r=0
if a1>a2:
    r=a1
else:
    r=a2
print('Max of two values =',r)
""
from pickletools import read_uint2

a1=8
a2=-4
a3=5
a4=1
r=0
if a1>a2 and a1>a3 and a1>a4: r=a1
elif a2>a1 and a2>a3 and a2>a4: r=a2
elif a3>a1 and a3>a2 and a3>a4: r=a3
else: r=a4
print('Max of four values is', r)

"""
"""
import math
a=-3
b=8
c=11
d=b**2-4*a*c
if d<0:
    r='There are no roots!'
else:
    x1=(-b-math.sqrt(d))/(2*a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    r='x1 =' +str(round(x1,3))+'\nx2 =' + str(round(x2,3))
print(r)
"""
"""
def alpha():
    s='Есдт хочешь быть красивым - поступай в гусары'
    return s
s=alpha()
print(s)
"""
"""
def beta(a,b):
    avg=(a+b)/2
    return avg
print(beta(10,20))
"""
a=(1,5,3,7,2,7.8,9)
print(a)
print(type(a))
print(a[0])
print(a[-1])
print(a[:3])
print(a[1:3])
print(a[3:])

