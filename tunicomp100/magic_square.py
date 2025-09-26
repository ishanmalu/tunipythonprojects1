"""
Checks whether a matrix is a magic square.
"""

def print_matrix(matrix, column_width):
    """Prints a matrix represented as nested lists to the screen. The rows
    of the matrix can be of different lengths. The parameter values are
    assumed to be valid.

    :param matrix: list, a matrix as a list of lists having integer elements.
    Sublists contain the rows of the matrix.
    :param column_width: int, the width of each column in characters.
    """

    # Print the matrix row by row.
    for row in matrix:
        # Print elements on the same line. Space is printed depending of
        # the column: The separating space is omitted, when the first column
        # is printed.
        first_column = True
        for element in row:
            if first_column:
                print(f"{element:{column_width - 1}}", end = "")
                first_column = False
            else:
                print(f"{element:>{column_width}}", end = "")
            
        # Start a new line only after all of the elements of the row have
        # been printed.
        print()

def is_magic_square(matrix, magic_constant):
    """Determines whether an matrix represented as nested list is a magic square,
    that is, a square matrix with the row and column sums equal to the magic
    constants. It is assumed that the matrix is a square and it contains values
    1, 2, ... n ** 2, where n is the length of the side.

    :param matrix: list, a as a list of lists. Sublists contain the rows of
    the matrix.
    :param magic_constant: int, the expected sum of elements of each row
    and column.
    :return: bool, True, if the matrix is a magic square. Otherwise, False is
    returned.
    """

    # Check row sums. The use of index is unnecessary, because the sum function
    # can be applied directly to sublists. False is returned, if an invalid row
    # is detected.
    for row in matrix:
        if sum(row) != magic_constant:
            return False

    # Check column sums. Two indices are used to demonstrate indexing better.
    # False is returned, if an invalid column is detected.
    length_of_side = len(matrix)
    for col_ind in range(0, length_of_side):
        # Compute a column sum. The column index is fixed, while the row index
        # changes. 
        col_sum = 0        
        for row_ind in range(0, length_of_side):
            col_sum += matrix[row_ind][col_ind]
        # Invalid column sum.
        if col_sum != magic_constant:
            return False

    # The matrix is a magic square, if we got here.
    return True

def main():
    # A 3 x 3 matrix made of a list of lists having integer elements.
    matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    # Print the matrix using two-digit wide columns.
    print_matrix(matrix, 2)
    # Test the matrix and print the result.
    has_magic = is_magic_square(matrix, 15)
    print("The matrix is ", end = "")
    if not has_magic:
        print("not ", end = "")
    print("a magic square.")
    
if __name__ == "__main__":
    main()
