def get_distance(point_1, point_2) -> float:
    distance = (((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5)
    return distance


def get_area_gerone(point_1, point_2, point_3) -> float:
    a = get_distance(point_1, point_2)
    b = get_distance(point_1, point_3)
    c = get_distance(point_2, point_3)
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


if __name__ == '__main__':
    assert abs(get_area_gerone((0, 0), (0, 4), (3, 0)) - 6.0 < 0.001)
    print('OK')
# пайтон смотрит в служебную переменную, смотрит, что этот файл был запущен как главный
