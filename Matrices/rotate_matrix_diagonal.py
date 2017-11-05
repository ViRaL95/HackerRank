import sys
def rotate_matrix():
    n = int(input())
    matrix = []
    new_matrix = []
    new_matrix = []
    for row in range(0, n):
        row_value = input()
        matrix.append(row_value.split(" "))
        new_matrix.append(row_value.split(" "))
    for row_index, row_value in enumerate(matrix):
        print(row_value)
        for indice_index, indice_value in enumerate(row_value):
            print(indice_value)
            if row_index != indice_index:
                new_matrix[indice_index][row_index] = matrix[row_index][indice_index]
                new_matrix[row_index][indice_index] = matrix[indice_index][row_index]
    return new_matrix
if __name__ == '__main__':
    matrix = rotate_matrix()

    for row in matrix:
        for column in row:
            print(column, end='')
        print("")
