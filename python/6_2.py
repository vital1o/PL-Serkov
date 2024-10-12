n = int(input("Введите количество элементов в массиве: "))  
array = [] # пустой список

for i in range(n):
    element = float(input("Введите элемент {}: ".format(i + 1)))
    array.append(element)

total = sum(array)  # Сумма массива
average = total / n  # среднее арифм

for i in range(n):
    if array[i] == 0:  # Проверяем, равен ли элемент нулю
        array[i] = average  # Заменяем нулевой элемент на среднее арифм

print("Среднее арифмитическое число:", average)
print("Изменённый массив:", array)
