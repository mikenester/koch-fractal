from math import *
from typing import List, Union, Tuple

import matplotlib.pyplot as plt
import numpy as np

from helpers import (
    get_third_vertex_coordinates,
    get_length,
    get_straight_line_coordinates,
    get_theta,
)
import config


def draw_line(a_coor: List[float], b_coor: List[float], iterations: int, ax):
    if iterations == 0:
        xpoints = np.array([a_coor[0], b_coor[0]])
        ypoints = np.array([a_coor[1], b_coor[1]])
        if config.MULTICOLOR:
            ax.plot(xpoints, ypoints)
        else:
            ax.plot(xpoints, ypoints, color=config.COLOR)
        return
    iterations -= 1
    length = get_length(a_coor, b_coor) / 3
    theta = get_theta(a_coor, b_coor)
    new_a_coor = a_coor
    new_b_coor = get_straight_line_coordinates(a_coor, length, theta)
    new_d_coor = get_straight_line_coordinates(new_b_coor, length, theta)
    new_c_coor = get_third_vertex_coordinates(new_b_coor, new_d_coor)
    new_e_coor = b_coor

    draw_line(new_a_coor, new_b_coor, iterations, ax)
    draw_line(new_b_coor, new_c_coor, iterations, ax)
    draw_line(new_c_coor, new_d_coor, iterations, ax)
    draw_line(new_d_coor, new_e_coor, iterations, ax)


def main():
    iterations = config.ITERATIONS
    if iterations < 0:
        raise ValueError("ITERATIONS must be a positive integer.")

    fig, ax = plt.subplots()

    # starting coordinates
    init_length = 1
    a_coor = [-0.5 * init_length, init_length / (2 * sqrt(3))]  # center on origin
    b_coor = get_straight_line_coordinates(a_coor, init_length, 0)
    c_coor = get_straight_line_coordinates(a_coor, init_length, -pi / 3)

    draw_line(a_coor, b_coor, iterations, ax)
    draw_line(b_coor, c_coor, iterations, ax)
    draw_line(c_coor, a_coor, iterations, ax)

    ax.set_aspect("equal", adjustable="datalim")
    ax.autoscale()
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    x_range = x_max - x_min
    y_range = y_max - y_min

    # Adjust the limits to center the origin
    ax.set_xlim(x_min - x_range * 0.1, x_max + x_range * 0.1)
    ax.set_ylim(y_min - y_range * 0.1, y_max + y_range * 0.1)

    plt.show()


if __name__ == "__main__":
    main()
