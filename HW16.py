# задание 16-1
print('задание 16-1')
import re
def abbreviation(letter):
     lst = re.findall(r'\b[а-яА-Я]', letter)
     result = (''.join(lst)).upper()
     return(result)
text = input('Введите название: ')
print(abbreviation(text))

print()

# задание 16-3
print('задание 16-3')
def uppercase_deco(func):
    def wrapper():
        or_res = func()
        modi = or_res.lower()
        return modi
    return wrapper
def h():
    return input('Введите слова: ')
h = uppercase_deco(h)
print(h())
