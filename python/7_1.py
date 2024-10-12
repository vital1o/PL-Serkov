print("Выберите фигуру для вычисления площади:")
print("1. Квадрат")
print("2. Прямоугольник")
print("3. Треугольник")

choice = int(input("Введите номер фигуры (1-3): "))

if choice == 1: 
    side = float(input("Введите сторону квадрата: ")) 
    area = side * side
    print("Площадь квадрата равна:", area)

elif choice == 2:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = length * width
    print("Площадь прямоугольника равна:", area) 

elif choice == 3:
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = 0.5 * base * height
    print("Площадь треугольника равна:", area)

else:
    print("Неверный выбор. Выберите номер от 1 до 3.") 