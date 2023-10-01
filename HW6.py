# задание 6-1 перевод римских цифр в десятичные числа
print('задание 6-1')
# input_number = input('Введите римскую цифру: ')
# dct = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# output_number = []
# if input_number.startswith(X):
#     print(dct.get('X'))
print()

# задание 6-2 считаем число книг прочитанных двумя учениками
# Война и мир, Над пропастью во ржи, Мастер и Маргарита, Идиот
# Евгений Онеги, Идиот, Мастер и Маргарита, Война и мир
# Контрольный ответ - 3
print('задание 6-2')
student_1 = input('Ввод книг прочитанных 1м учеником: ').split(', ')
student_2 = input('Ввод книг прочитанных 2м учеником: ').split(', ')
identical_elements = []
for item in student_1:
    if item in student_2:
        identical_elements.append(item)
# print(identical_elements, type(identical_elements))
print('Количество книг, которые прочитали оба ученика: ', len(identical_elements))

# задание 6-3
# вход - строка из символов
# выход - 3 строки: буквы, цифры, уникальные знаки
input_str = str(input('Введите строку: '))
sorted_str = set(input_str)
sorted_str = sorted(sorted_str)
letters = []
numbers = []
symbols = []
for i in sorted_str:
    if i.isalpha():
        letters.append(i)
    elif i.isnumeric():
        numbers.append(i)
    elif i.isascii():
        symbols.append(i)
print(*letters, sep=', ')
print(*numbers, sep=', ')
print(*symbols, sep=', ')
