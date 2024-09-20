A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A < B:
    for num in range(A, B + 1):
        print(num)
else:
    for num in range(A, B - 1, -1):
        print(num)
