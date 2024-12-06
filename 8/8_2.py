import random

N = int(input("Введите значение N: "))
M = int(input("Введите значение M: "))

# Генерация матрицы B
B = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]

print("Исходная матрица B:")
for row in B:
    print(row)

for i in range(N):
    max_index = 0
    min_index = 0
    for j in range(1, M):
        if B[i][j] > B[i][max_index]:
            max_index = j
        if B[i][j] < B[i][min_index]:
            min_index = j
    
    B[i][0], B[i][max_index] = B[i][max_index], B[i][0]
    B[i][-1], B[i][min_index] = B[i][min_index], B[i][-1]

print("Матрица B после замены:")
for row in B:
    print(row)