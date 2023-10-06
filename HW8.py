# задача 8-1
print("задача 8-1")
def correct_genetic_code(code):
    corrected_code = ""  # Переменная для хранения исправленного генетического кода
    i = 0  # Счетчик для итерации по коду
    while i < len(code):  # Пока не достигли конца кода
        if i < len(code)-1:  # Проверяем, что текущий символ - не последний в коде
            if (code[i] == 'А' and code[i+1] == 'Г'):
                # Если текущий символ 'А' и следующий 'Г',
                # добавляем "ГА" в исправленный код и увеличиваем счетчик на 2
                corrected_code += "ГА"
                i += 2
            elif (code[i] == 'Г' and code[i+1] == 'А'):
                # Если текущий символ 'Г' и следующий 'А',
                # добавляем "АГ" в исправленный код и увеличиваем счетчик на 2
                corrected_code += "АГ"
                i += 2
            elif code[i] == 'Ц' and code[i+1] == 'Т':
                # Если текущий символ 'Ц', а следующий 'Т',
                # добавляем "ЦАГТ" в исправленный код и увеличиваем счетчик на 2
                corrected_code += "ЦАГТ"
                i += 2
            elif code[i] == 'Т' and code[i+1] == 'Ц':
                # Если текущий символ 'Т', а следующий 'Ц',
                # добавляем "ТАГЦ" в исправленный код и увеличиваем счетчик на 2
                corrected_code += "ТАГЦ"
                i += 2
            else:
                # Если ни одно из условий не выполняется, то добавляем текущий символ в исправленный код
                corrected_code += code[i]
                i += 1
        else:
            # Если текущий символ последний в коде, добавляем его в исправленный код и увеличиваем счетчик на 1
            corrected_code += code[i]
            i += 1
    return corrected_code
print("Исправленный генетический код: ", correct_genetic_code(input("Введите генетический код: ")))
print()

# задача 8-2
print("задача 8-2")
def sort_lists(lst):
    lst.sort(key=lambda x: (sum(int(str(n)) for n in x), x), reverse=True)  # Сортировка по общей сумме чисел и самого списка
    for sublist in lst:
        sublist.sort(reverse=True)  # Сортировка каждого подсписка по убыванию
    return lst

sorted_list = sort_lists([[1, 6, 4], [1, 2], [5, 88, 67, 666]])
print("Отсортированный список:")
for sublist in sorted_list:
    print(sublist)
print()

# задача 8-3
print("задача 8-3")
def sort_words(word_list):
    #Используем метод sort() со специальным ключом key для определения порядка сортировки
    word_list.sort(key=lambda x: (-len(set(x)), x))
    return word_list

sorted_words = sort_words(['abcden', 'xx', 'abdcen', 'abcbab'])
print("Отсортированный список слов:")
print(sorted_words)
