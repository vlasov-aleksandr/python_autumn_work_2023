# задание 15-1
print('задание 15-1')
res=[]
def dctkey(dct):
    for k,v in dct.items():
        if k == x:
            res.append(v)
        if type (v) == dict:
            dctkey(v)
    return res
dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11, 6:22}}
x = key
print(dctkey(dct))

print()

# задание 15-2
print('задание 15-2')
import re
def gosnomer(x):
    lst = '[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]\d\d\d[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]{2}1?78'
    result = re.findall(lst, x)
    return result


s = 'X777XX777 Н383РС178 Mercedes W245 A759РХ78 О412ТУ47 A178BC78 1Г.270.356'
print(gosnomer(s))

print()

# задание 15-3
print('задание 15-3')
import re
def phone_find(x):
    lst = '\+7\(812\)\d{3}-\d{4}|\+7\(921\)\d{3}-\d{4}|\+7\(812\)\d{3}-\d{2}-\d{2}|\+7\(921\)\d{3}-\d{2}-\d{2}'
    result = re.findall(lst, x)
    return result

phone_numbers = "7(812)111-1111 +7(812)222-22-22 +7(921)333-3333 +7(921)444-44-44 +79215555555 +7(812)6H 812-921-812-777 +79218888888"
print(phone_find(phone_numbers))
