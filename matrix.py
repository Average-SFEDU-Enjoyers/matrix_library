#! Библиотека для работы с матрицами

def transpose(matrix):
    """
    Функция для транспонирования матрицы. На вход принимает параметром двумерный список list
    :param matrix:
    :return: transpose_matrix
    """
    transpose_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix


def matrix_multiplication(matrix1, matrix2):
    """
    Функция для умножения матриц друг на друга. Если матрицы не удовлетворяет математическим условиям
    :param matrix1: первая матрица типа m × n (т.е. m строк и n столбцов)
    :param matrix2: вторая матрица (b) типа n × k.
    :return: матрица m × k
    """
    m = len(matrix1)
    n = len(matrix2)
    k = len(matrix2[0])
    multiplication_matrix = [[0 for j in range(k)] for i in range(m)]
    for i in range(m):
        for j in range(k):
            for kk in range(n):
                multiplication_matrix[i][j] += matrix1[i][kk] * matrix2[kk][j]
    return multiplication_matrix


def multiplication_matrix_scalar(matrix, number=2):
    """
    Функция для умножения матрицы на число. Принимает на вход матрицу и число на которое надо умножить
    :param matrix: исходная матрица
    :param number: число на которое надо умножить
    :return: матрица после умножения
    """
    multiplication_matrix = [[1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    a = len(matrix)
    b = len(matrix[0])
    for i in range(a):
        for j in range(b):
            multiplication_matrix[i][j] = matrix[i][j] * number
    return multiplication_matrix


def matrix_print(matrix, width=3):
    """
    Функция для печати матрицы. На вход принимает двумерный список list.
    :param matrix:
    :param width: сколько символов будет выделенно на каждый элемент(включая скобки)
    :return:
    """
    for i in matrix:
        for j in i:
            print(str.center("[%d]" % j, width), end='')
        print()
