import numpy as np

N = int(input("Введите значение N: ")) 
A = np.random.randint(-10, 10, size=(N, N))

sum_positive = 0
count_positive = 0

for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] > 0:
            sum_positive += A[i][j] 
            count_positive += 1  

print("Матрица A:")
print(A)
print("Сумма положительных элементов над главной диагональю:", sum_positive)
print("Количество положительных элементов над главной диагональю:", count_positive)
