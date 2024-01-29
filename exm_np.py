import numpy as np
my_array = np.arange(10)
print("Исходный массив:", my_array)
print("Элементы с индексами от 3 до 6:", my_array[3:7])
my_array[7:10] = [10, 20, 30]
print("Измененный массив:", my_array)


