def calculate_sum_and_average(array):
    total = sum(array)
    average = total / len(array) if len(array) > 0 else 0
    return total, average  

arrays = []
for i in range(3):
    print("Введите элементы массива {} (через пробел):".format(i + 1))
    array = list(map(int, input().split()))
    arrays.append(array)

for i, array in enumerate(arrays):
    total, average = calculate_sum_and_average(array) 
    print("Массив {}: Сумма = {}, Среднее арифметическое = {}".format(i + 1, total, average)) 
