n = int(input("Введите количество элементов в массиве: "))
array = [] # пустой список

for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)

max_element = max(array)
print("Максимальный элемент:", max_element)

print("Массив в обратном порядке:", array[::-1])