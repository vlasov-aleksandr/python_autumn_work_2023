# задача 12-1
print('задача 12-1')
def minimax(x):
  return [i for i in range(0,len(x)) if x[i] == min(x)], [j for j in range(0,len(x)) if x[j] == max(x)]
x = list(map(int, input('введите целые числа: ').split()))
print (minimax(x))
print()

# задача 12-2
print('задача 12-2')
print([i for i in range(1, 11) for j in range(i)])
print()

# задача 12-3
print('задача 12-3')
def num_func(x):
    s = [[int(a) for a in b.split('-')] for b in x.split(',')]
    return [i for num in s for i in range(num[0], num[1] + 1)]
s = '1-2,4-4,99-102'
print(num_func(s))
