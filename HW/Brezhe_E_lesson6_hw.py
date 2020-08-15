# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения. Задание сделать с использованием enumerate.
my_list = ['jsbd', 'lvk', 'halehbr', 'geargae']
new_list = []
for index, value in enumerate(my_list):
    if index % 2:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)
############################################

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ['aaa', 'bbb', 'ccc', 'abc', 'a123']
new_list = [value for value in my_list if value[0:1] == 'a']
print(new_list)
############################################

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ['aaa', 'bab', 'ccc', 'bca', '123a']
new_list = [value for value in my_list if 'a' in value]
print(new_list)
############################################

# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.
my_list = ['aaa', 123, 'ccc', 456, '123']
new_list = [value for value in my_list if type(value) == str]
print(new_list)
############################################

# 5. Дана строка my_str. Вывести символы, которые встречаются в строке только один раз.
my_str = 'QWEqwerty_qwe'
for value in my_str:
    if my_str.count(value) == 1:
        print(value)
############################################

# 6. Даны две строки, вывести те символы, которые есть в обеих строках.
my_str_1 = 'QWERTy'
my_str_2 = 'qwerty'
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
print(my_set_1.intersection(my_set_2))
############################################

# 7. Даны две строки, вывести те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
my_str_1 = 'QWERTYqwertyQWERTY'
my_str_2 = 'qwerty_qwe'
my_list_1 = []
my_list_2 = []
for value in my_str_1:
    if my_str_1.count(value) == 1:
        my_list_1 += value
for value in my_str_2:
    if my_str_2.count(value) == 1:
        my_list_2 += value
my_set_1 = set(my_list_1)
my_set_2 = set(my_list_2)
print(my_set_1.intersection(my_set_2))
############################################

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
person = {"Фамилия": "Иванов",
          "Имя": "Иван",
          "Возраст": "105",
          "Проживание": {
            'Страна': 'Украина',
            'Город': 'Днепр',
            'Улица': 'Яворницкого'},
          "Работа": {
              "Наличие": "Нет",
              "Должность": "-"
          }}
############################################

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта, придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
recipe = {"Составляющие": {
    "Коржи": {
        "Мука": "0,5 кг",
        "Молоко": "100 гр",
        "Масло": "200 гр",
        "Яйцо": "4 шт"},
    "Крем": {
        "Сахар": "200 гр",
        "Масло": "100 гр",
        "Ваниль": "0,5 пакетика",
        "Сметана": "200 гр"},
    "Глазурь": {
        "Какао": "50 гр",
        "Сахар": "100 гр",
        "Масло": "100 гр"}
}}