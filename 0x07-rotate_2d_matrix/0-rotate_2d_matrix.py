#!/usr/bin/python3
"""This module provides a function
    to rotate a 2D matrix 90 degrees clockwise.
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list): The 2D matrix to rotate.
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
