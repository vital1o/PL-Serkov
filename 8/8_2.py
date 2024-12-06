import numpy as np

N = int(input("Введите значение N: "))
M = int(input("Введите значение M:")) 
B = np.random.randint(-10, 10, size=(N, M)) 

print("Исходная матрица B:")
print(B)

for i in range(N):
    max_index = np.argmax(B[i]) 
    min_index = np.argmin(B[i]) 
    
    B[i][0], B[i][max_index] = B[i][max_index], B[i][0]
    
    B[i][-1], B[i][min_index] = B[i][min_index], B[i][-1]

print("Матрица B после замены:")
print(B)