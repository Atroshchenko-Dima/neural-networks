import numpy as np

a = np.zeros((2,4))
b = np.zeros((4,3)) # матрица с 4 строками и 3 столбцами состоящая из нулей

c = a.dot(b) 
print(c.shape) # выведет(2,3)

h = np.zeros((5,4)).T # операция .T повернет(транспонирует) матрицу, поменяв строки и столбцы местами
i = np.zeros((5,6))
j = h.dot(i)
print(j.shape)