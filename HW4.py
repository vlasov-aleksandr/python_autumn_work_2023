# задание 4-1 - калькулятор v0.1
print('задание 4-1')
inp = tuple((input('ввод: ')).split(' '))
num1 = float(inp[0])
num2 = float(inp[2])
mo = inp[1]
if mo == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
if mo == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
if mo == '*':
    print(f'{num1} x {num2} = {num1 * num2}')
if num2 == 0 and mo == '/':
    print('ноль в знаменателе!')
elif mo == '/':
    print(f'{num1} / {num2} = {num1 / num2}')
print()

# задание 4-2 печатаем спираль из чисел
print('задание 4-2')
print('фокус не понят')
print()

# задание 4-3 ASD! ASD! ASD! / ASD! Das sad.
print('задание 4-3')
p = input('--> ')
q = input('--> ')
pp = {}
qq = {}
for i in p:
    if i.isalpha():
        i = i.lower()
        pp[i] = pp.get(i, 0) + 1
for j in q:
    if j.isalpha():
        j = j.lower()
        qq[j] = qq.get(j, 0) + 1
# print("22", pp)
# print("33", qq)
print(pp == qq)

