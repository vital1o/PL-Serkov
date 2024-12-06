from math import *

print('№1')

def f(x,n):
    return (x**n)/factorial(n)
a = int(input())
b = int(input())
print(f(a,b))

print('-'*6)

print('№3')
def f(n):
    a = n[::-1]
    return a
print(f(input()))
#block B

def dev(n, divisor):
  if n <= 1:
    return False
  if divisor * divisor > n:
    return True
  if n % divisor == 0:
    return False
  return dev(n, divisor + 1)

n = int(input("Введите натуральное число n>1: "))

if dev(n, 2):
  print("Да")
else:
  print("Нет")