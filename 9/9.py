def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_expression(x, n):
    x_power_n = x ** n
    n_fact = factorial(n)
    result = x_power_n / n_fact
    print(f"x^n = {x_power_n}")
    print(f"n! = {n_fact}")
    return result

try:
    x = int(input("Введите натуральное число X: "))
    n = int(input("Введите натуральное число N: "))

    if x <= 0 or n < 0:
        raise ValueError("Оба числа должны быть натуральными.")
    
    result = calculate_expression(x, n)
    print(f"Результат выражения x^n / n! для X = {x} и N = {n} равен: {result}")

except ValueError as e:
    print(f"Ошибка ввода: {e}")
#block B

def find_max():
    number = int(input("Введите натуральное число (0 для завершения): "))
    
    if number == 0:
        return -1
    
    max_of_rest = find_max()
    
    if max_of_rest == -1:
        return number
    else:
        return max(number, max_of_rest)
        
max_value = find_max()
print(f"Наибольшее значение в последовательности: {max_value}")