# задание 3-1
print('задание 3-1')
lst1 = []
i = 0
while True:
    lst1.append(float(input('введите мне зарплату: ')))
    if lst1[-1] == 0: break
lst1.pop(-1)
zp = sum(lst1) / len(lst1)
print('средняя зарплата - ', zp)
print()

# задание 3-2
print('задание 3-2')
num = str(int(input('введите целое число --> ')))
for i in range(10):
    print(f'{i} - {num.count(str(i))}')
print()

# задание 3-3
print('3-3')
s = (input('введите предложение: ')).split(' ')
max_len = max(len(word) for word in s)
lngwrd = [word for word in s if len(word) == max_len]
print('ТОП самых длинных слов:', ', '.join(lngwrd))

