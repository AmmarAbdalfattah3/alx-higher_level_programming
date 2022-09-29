#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rx = list(map(lambda my_list: [item ** 2 for item in my_list], matrix))
    return rx
