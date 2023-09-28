# задание 5-1 треугольник Паскаля
print('задание 5-1')
num_str = int(input('введите число строк треугольника Паскаля: '))
if num_str <= 0:
    print('Треугольника с таким числом строк не существует.')
else:
    for i in range(1, num_str+1):
        first_num = 1
        print()
        for j in range(1, i+1):
            print(first_num, end=' ')
            first_num = first_num * (i - j) // j
print()
print()

# задание 5-2 ввести число, напечатать делители
print('задание 5-2')
n = int(input('Введите число: '))
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)
print(*lst, sep=', ')
print()

# задание 5-3 число Фибаначи
print('задание 5-3')
n = int(input('Введите число: '))
f = [1, 1]
for i in range(2, n):
    f.append(f[i - 1] + f[i - 2])
print(*f, sep=', ')

