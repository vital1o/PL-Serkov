# block a
from math import *
print('№1')
def f(x,n):
    return (x**n)/factorial(n)
a = int(input("Введите значение: "))
b = int(input("Введите значение: "))
print(f(a,b))

print('-'*6)

print('№3')
def f(n):
    a = n[::-1]
    return a
print(f(input()))

#block b

def prosto(n, divisor):
  if n <= 1:
    return False
  if divisor * divisor > n:
    return True
  if n % divisor == 0:
    return False
  return prosto(n, divisor + 1)

n = int(input("Введите натуральное число n>1: "))

if prosto(n, 2):
  print("Да")
else:
  print("Нет")