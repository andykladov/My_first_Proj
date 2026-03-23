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
"""
a=(1,5,3,7,2,7.8,9)
print(a)
print(type(a))
print(a[0])
print(a[-1])
print(a[:3])
print(a[1:3])
print(a[3:])
"""
"""
def delta(a,b):
    s=a+b
    v=s/2
    return s,v
b1,b2=delta(10,20)
b=delta(10,20)
print('sum = ',b1, 'aver = ', b2)
print('sum = ',b[0], 'aver = ', b[1])
"""
import random
n=random.randint(1,7)
print(n)

import random
def ger_world(n):
    if n==1: s= 'Камень'
    elif n == 2: s = 'Ножн'
    else: s ='Бумага'
    return s
def game (word):
    n = random.randint(1, 3)
    pc=ger_world(n)
    r1='Пользователь : ' + word + ',Компьютер: ' + pc
    if word=='Камень' and pc=='Ножн':
        r2='Выигр пользователь, т.к. камень ломает ножн'
    elif word == 'Ножн' and pc == 'Бумага':
        r2 = 'Выигр пользователь, т.к. ножн режут бумагу'
    elif word == 'Бумага' and pc == 'Камень':
        r2 = 'Выигр пользователь, т.к. бумага  заворачивает камень'
    elif word=='Ножн' and pc=='Камень':
        r2='Выигр комп, т.к. камень ломает ножн'
    elif word == 'Бумага' and pc == 'Ножн':
        r2 = 'Выигр комп, т.к. ножн режут бумагу'
    elif word == 'Камень' and pc == 'Бумага':
        r2 = 'Выигр комп, т.к. бумага  заворачивает камень'
    else: r2='Ничья'
    return r1 +'\n' +r2 + '\n'
#print(ger_world(1))
#print(ger_world(2))
#print(ger_world(3))

print(game('Камень'))
print(game('Ножн'))
print(game('Бумага'))





