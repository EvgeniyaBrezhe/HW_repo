from uti
# Функция - действие, у нее есть аргументы, она что-то может возвращать, а может ничего не возвращать

point_A = (10, 1)
point_B = (10, 2)
point_C = (9, 1)

distance_AtoB = get_distance(point_A, point_B)
print(distance_AtoB)

# надо следить за тем, что возвращает функция (тип) '-> float:' - явная типизация позволяет ловить ошибки в процессе
# разработки

area_ABC = get_area_gerone(point_A, point_B, point_C)
print(area_ABC)

# результат отличается от 0.5 из-за особенностей хранения float в памяти

if area_ABC == 0.5:
    print('ok')
else:
    print('not ok')

# float-ы сравниваются только через вычитание
# a == b - ПЛОХОЙ СПОСОБ
# abs(a - b) < 0.0001 - ПРАВИЛЬНО

if abs(area_ABC - 0.5) < 0.001:
    print('ok')
else:
    print('not ok')

assert abs(area_ABC - 0.5) < 0.001
print(area_ABC)
# если тру - то программа идет дальше, как мембрана, пропускающая одни частицы, и не пропускающая другие,
# если нет, что AssertionError
# нельзя использовать для проработки логики
assert abs(get_area_gerone((0, 0), (0, 4), (3, 0)) - 6.0 < 0.001)
print(area_ABC)