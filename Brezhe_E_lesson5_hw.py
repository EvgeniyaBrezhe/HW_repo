# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# my_number = 123000000000321
# counter = 0
# for index in str(my_number):
#     if index == '0':
#         counter +=1
# print(counter)
############################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
my_number = 100100
counter = 0
while index in str(my_number[::-1]):

############################################
# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить четные элементы из my_list_1
# и потом нечетные элементы из my_list_2.

############################################
# 4. Дан список my_list. Создать список new_list у которого первый элемент из my_list стоит на последнем месте.
# Если my_list [1,2,3,4], то new_list [2,3,4,1]

############################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место. [1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя!

############################################
# 6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
# Найти сумму ВСЕХ чисел в этой строке. Для данного примера 133.

############################################
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
# подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']

############################################
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить часть строки
# между этими символами. my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

############################################
# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть
# строки между этими символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

############################################
# 10. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа),
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно
# соседей. Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
