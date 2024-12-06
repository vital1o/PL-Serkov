n = 4
a = []
with open("vvod.txt") as file:
    for line in file:
        arr = [int(x.strip()) for x in line.split()]
        a.append(arr)

print('Исходный массив:')
for i in a:
    print(*i)

for i in range(n-1):
    for j in range(n):
        a[i][j] -=a[n-1][j]
arr = a
print('-'*8)
file_v = open('vivod.txt','w')
file_v.write(str(arr))
file_v.close()
for i in arr:
    print(*i)