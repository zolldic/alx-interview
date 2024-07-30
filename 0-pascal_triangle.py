#!/usr/bin/python3
""" Pascal's Triangle """


def factorial(n):
    """
    Calculate the factorial of n
    """
    if n == 0 or n == 1:
        return (1)
    return (n * factorial(n - 1))


def pascal_triangle(n):
    """
        Generate Pascal's Triangle up to the nth row.
        Args:
            n (int): number of rows
    """

    traingle = []
    for idx in range(n):
        list_of_elements = []
        row_factorial = factorial(idx)

        for k in range(0, idx + 1):
            # calc the element at position k
            element = row_factorial // (factorial(k) * factorial(idx-k))

            # append the element into a list
            list_of_elements.append(element)

        traingle.append(list_of_elements)

    return traingle
