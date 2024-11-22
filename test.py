import logging
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


def main():
    fig, ax = plt.subplots()

    # starting coordinates
    a_coor = [2, 2]
    b_coor = [4, 4]
    c_coor = get_third_vertex_coordinates(a_coor, b_coor)

    length_a_b = get_length(a_coor, b_coor)
    length_b_c = get_length(b_coor, c_coor)
    length_c_a = get_length(c_coor, a_coor)

    print("length_a_b:", length_a_b)
    print("length_b_c:", length_b_c)
    print("length_c_a:", length_c_a)

    xpoints = np.array([a_coor[0], c_coor[0], b_coor[0]])
    ypoints = np.array([a_coor[1], c_coor[1], b_coor[1]])
    ax.plot(xpoints, ypoints)

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
