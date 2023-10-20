# задание 14-1
print('задние 14-1')
def num_count(n):
  if n < 10:
    return 1
  else:
    return 1 + num_count(n // 10)
print(num_count(int(input('Введите натуральное число:'))))

print()

# задание 14-2
print('задние 14-2')
def num_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + num_sum(n // 10)
print(num_sum(int(input('Введите натуральное число:'))))

print()

# задание 14-3
print('задние 14-3')
def double_triangle(n):
    print('*' * n)
    if n > 1:
        double_triangle(n - 1)
        print('*' * n)
double_triangle(int(input('Введите число: ')))