from math import *
from typing import List, Tuple

import config


def get_third_vertex_coordinates(a_coor: List[int], b_coor: List[int]) -> Tuple[int]:
    length = get_length(a_coor, b_coor)

    theta = get_theta(a_coor, b_coor)

    c_x = get_third_vertex_x_coordinate(length, a_coor, theta)
    c_y = get_third_vertex_y_coordinate(length, a_coor, theta)

    c_coor = [c_x, c_y]

    if config.DEBUG:
        print(f"Coordinates: {a_coor}, {b_coor}, {c_coor}")

    return c_coor


def get_theta(a_coor: List[int], b_coor: List[int]) -> Tuple[int]:
    length = get_length(a_coor, b_coor)
    a_x = a_coor[0]
    a_y = a_coor[1]
    b_x = b_coor[0]
    b_y = b_coor[1]

    if b_x == a_x and b_y > a_y:
        theta = pi / 2
    elif b_x == a_x and b_y < a_y:
        theta = 3 * pi / 2
    elif b_y >= a_y and b_x > a_x:
        # quadrant 1
        theta = atan((b_y - a_y) / (b_x - a_x))
    elif b_y >= a_y and b_x < a_x:
        # quadrant 2
        theta = (pi / 2) + asin((a_x - b_x) / length)
    elif b_y < a_y and b_x < a_x:
        # quadrant 3
        theta = pi + asin((a_y - b_y) / length)
    else:
        # quadrant 4
        theta = (3 * pi / 2) + asin((b_x - a_x) / length)

    if config.DEBUG:
        print(f"theta: {theta} -- {theta / pi}π")

    return theta


def get_straight_line_coordinates(
    a_coor: List[float], length: float, theta: float
) -> List[float]:
    """
    @param a_coor: starting coordinates - [1.34, -345.3]
    @param length: length of line
    @param theta: Angle of line in radians
    """
    x = a_coor[0]
    y = a_coor[1]

    new_x = x + (cos(theta) * length)
    new_y = y + (sin(theta) * length)

    return [new_x, new_y]


def get_length(a_coor: List[float], b_coor: List[float]):
    a_x = a_coor[0]
    a_y = a_coor[1]
    b_x = b_coor[0]
    b_y = b_coor[1]

    length = sqrt(pow((b_x - a_x), 2) + pow((b_y - a_y), 2))

    if config.DEBUG:
        print(f"length: {length}")

    return length


def rotate_x(length, theta):
    return length * (cos(theta) - (sqrt(3) * sin(theta))) / 2


def rotate_y(length, theta):
    return length * (sin(theta) + (sqrt(3) * cos(theta))) / 2


def get_third_vertex_x_coordinate(
    length: int, a_coor: List[float], theta: float
) -> int:
    a_x = a_coor[0]
    return rotate_x(length, theta) + a_x


def get_third_vertex_y_coordinate(
    length: int, a_coor: List[float], theta: float
) -> int:
    a_y = a_coor[1]
    return rotate_y(length, theta) + a_y
