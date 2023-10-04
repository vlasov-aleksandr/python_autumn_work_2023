# задание 7-1 НОК списка чисел
# print('7-1')
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

# задание 7-3 вообще не пон
print('задание 7-3')


