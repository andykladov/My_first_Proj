"""
import numpy as np

# Координаты потребителя
x = 730000
y = 5440000
z = 3230000
# Координаты первого спутника
x0 = 15524471.175
y0 = 16649826.222
z0 = 13512272.387

# Координаты второго спутника
x1 = 2304058.534
y1 = 23287906.465
z1 = 11917038.105

# Координаты третьего спутника
x2 = 16680243.357
y2 = 3069625.561
z2 = 20378551.047

# Координаты четвертого спутника
x3 = 14799931.395
y3 = 21425358.24
z3 = 6069947.224
A = np.ones((4, 4))
print(A)
r0 = np.sqrt((x0 - x) ** 2 + (y0 - y) ** 2 + (z0 - z) ** 2)
r1 = np.sqrt((x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2)
r2 = np.sqrt((x2 - x) ** 2 + (y2 - y) ** 2 + (z2 - z) ** 2)
r3 = np.sqrt((x3 - x) ** 2 + (y3 - y) ** 2 + (z3 - z) ** 2)

A[0, 0] = (x0 - x) / r0
A[0, 1] = (y0 - y) / r0
A[0, 2] = (z0 - z) / r0
A[1, 0] = (x1 - x) / r1
A[1, 1] = (y1 - y) / r1
A[1, 2] = (z1 - z) / r1
A[2, 0] = (x2 - x) / r2
A[2, 1] = (y2 - y) / r2
A[2, 2] = (z2 - z) / r2
A[3, 0] = (x3 - x) / r3
A[3, 1] = (y3 - y) / r3
A[3, 2] = (z3 - z) / r3
print(A)
Q = np.linalg.inv(A.T.dot(A))
print(Q)
VDOP = np.sqrt(Q[2, 2])
HDOP = np.sqrt(Q[0, 0] + Q[1, 1])
TDOP = np.sqrt(Q[3, 3])
PDOP = np.sqrt(Q[0, 0] + Q[1, 1] + Q[2, 2])
GDOP = np.sqrt(PDOP ** 2 + TDOP ** 2)
print('VDOP=', VDOP)
print('HDOP=', HDOP)
print('TDOP=', TDOP)
print('PDOP=', PDOP)
print('GDOP=', GDOP)
"""
from operator import index
from unittest.mock import inplace

import pandas as pd
SureName=['Гальцев','Дорохин','Васильев']
Age=[26,28,30]
Position=['Моряк','Матрос','Юнга']
df1=pd.DataFrame([SureName,Age,Position])
df1=df1.T
df1.columns=['Фамилия','Возраст','Должность']
print(df1)
print(df1.shape)
print(df1.columns)
print(df1.iloc[1])
print(df1[['Фамилия','Должность']]) #отобразить список всех фамилий
print(df1.iloc[:,0])#по индексу
print(df1.iloc[:,-1])
#print(df1.iloc[:,0:,-1]) #все кроме последнего - УТОЧНИТЬ ЧТО не так!!!
df1['Хобби']=['Макраме','Вязание','Рыбалка']#добавляем столбец
print(df1)
df1.loc[len(df1)]=['Валев', 41, 'Повар','Танцы']
print(df1)
df1.drop(index=2, inplace=True)
print(df1)



