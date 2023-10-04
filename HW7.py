# задание 7-1 НОК списка чисел
print('7-1')
# def HOK_func(*args):
#     x = max(args)
#     args.remove(x)
#     y = max(args)
#     while(True):
#         if((greater % x == 0) and(greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
# n = int(input('--> '))
# print(HOK_func(n))
# код не доделан, сейчас не работает

# перемножаем все числа
# произведение поочереди делится на каждое из чисел
# не очень мощное, но самое короткое решение
s = list(map(int, input('-->').split()))
res = 1
for k in s:
    res *= k
for n in range(res, 0, -1): # в обратном порядке (с конца)
    # идем с произведения, с шагом -1
    for m in s:
        if n % m: break
    else:
            nok = n
print(nok)

# еще вариант
# алгоритм Евклида
s = list(map(int, input('-->').split()))
def nod(a,b): # алгоритм Евклида
    while a !=0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
def nok2(a, b):
    return a * b // nod(a, b)

x = 1
for i in s:
    x = nok2(x, i)
print(x)

# задание 7-2 Шифр цезаря со сдвигом n
# без знаков препинания и пробелов(
print('7-2')
def code(string, n):
    result = ""
    for i in range(len(string)): 
        char = string[i] 
        if(char.isupper()): 
            result += chr((ord(char) + (n-1) - 64) % 26 + 65) 
        else: 
            result += chr((ord(char) + (n-1) - 96) % 26 + 97) 
    return result 
string = str(input('input messege: '))
n = int(input('key: '))
print("Plain txt : " + string) 
print("Shift pattern : " + str(n)) 
print("Cipher: " + code(string, n)) 

# правильный рабочий способ
def code(string, n):
    res = ''
    for i in string:
        new_ord = ord(i) + n
        if chr(ord('a')) <= i <= chr(ord('a') + 25):
            new_ord = ord('a') + (new_ord - ord('a')) % 26
            res += chr(new_ord)
        elif chr(ord('A')) <= i <= chr(ord('A') + 25):
            new_ord = ord('A') + (new_ord - ord('A')) % 26
            res += chr(new_ord)
        else:
            res += i
    return res
while True:
    print(code(input('code: '), int(input('n: '))))
# опа опа, у 7-2 нету тормозов (бесконечный цикл, без выхода)
# задание 7-3 вообще не пон
print('задание 7-3')
lst = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [1,2,3,4]]
# упрощенка без input
cmn = []
for i in lst:
    cmn.extend(i)
print(sorted(cmn)[-3:])

# вариант через append
lst = [[1, 2, 3], [4,5,6]]
cmn = []
for i in lst:
    for j in i:
        cmn.append(j)
print("res=", sorted(cmn)[-3:])