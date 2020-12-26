'''
    This class represents a matrix and has implementations of common methods 
    associated with matrices
'''
class Matrix:
    
    # The number of rows in the matrix
    __rows = 0

    # The number of columns in the matrix
    __columns = 0

    # The matrix's elements
    __data = []

    '''
        Create a new matrix by passing a 2D list of data
        
        Keyword arguments:
        data -- the elements of the matrix
    '''
    def __init__(self, data):
        self.__rows = len(data)
        self.__columns = len(data[0])
        self.__data = data

    ''' Returns a string presentation of the matrix '''
    def __str__(self):
        return self.__data

    ''' Get number of rows '''
    def num_rows(self):
        return self.__rows

    ''' Get number of columns '''
    def num_columns(self):
        return self.__columns

    ''' Get matrix data'''
    def get_data(self):
        return self.__data

    '''
        Determine whether the matrix is a square matrix

        Returns:
        bool -- true if the matrix is square, false otherwise
    '''
    def is_square_matrix(self):
        return self.__rows == self.__columns

    '''
        Determine whether the matrix has same number of rows and columns as the given matrix

        Keyword arguments:
        matrix -- the other matrix to compare to

        Returns:
        bool -- the truth value of the test
    '''
    def is_equal_to(self, matrix):
        if(self.__rows != matrix.num_rows() or 
                self.__columns != matrix.num_columns()):
        
            return False
        
        return True

    '''
        Determine if a given matrix has exactly the same elements as this matrix

        Keyword arguments:
        matrix -- the other matrix to compare to

        Returns:
        bool -- the truth value of the test
    '''
    def is_equivalent_to(self, matrix):
        if(not self.is_equal_to(matrix=matrix)):
            return False
        
        matrix_data = matrix.get_data()

        for i in range(self.__rows):
            for j in range(self.__columns):
                if self.__data[i][j] != matrix_data[i][j]:
                    return False

        return True

    '''
        Determine whether a given row contains zero elements throughout

        Keyword arguments:
        row -- the row list to check

        Returns:
        bool -- the truth value of the test
    '''
    def is_zero_row(self, row):
        for value in row:
            if value != 0:
                return False

        return True

    '''
        Get the first non zero element in a given row

        Keyword argument:
        row -- the row list

        Returns:
        float -- the first non-zero element or -1 if non-zero element is not found
    '''
    def get_first_non_zero_of_row(self, row):

        for value in row:
            if value != 0:
                return value
        
        return -1

    '''
        Get the position of the first non-zero element in a given row

        Keyword arguments:
        row -- the row list

        Returns:
        int -- the position of the first non-zero element in the row or -1 if non-zero element is not found
    '''
    def get_position_of_first_non_zero_of_row(self, row):
        for index, value in row:
            if value != 0:
                return index
        
        return -1

    '''
        Determine the feasibility of a multiplication between this matrix and the given matrix 

        Keyword arguments:
        matrix -- the matrix to compare to

        Returns:
        bool -- the truth value of this test
    '''
    def can_multiply(self, matrix):
        return self.__columns == matrix.num_rows()

    '''
        Determine whether the matrix is in echelon form

        Returns:
        bool -- the truth value of this test
    '''
    def is_in_echelon_form(self):
        for i in range(self.__rows):
            if self.is_zero_row(self.__data[i]):
                for j in range(i+1, self.__rows):
                    if not self.is_zero_row(self.__data[j]):
                        return False
            
            else:
                position = self.get_position_of_first_non_zero_of_row(self.__data[i])

                if i > 0 and position < self.get_position_of_first_non_zero_of_row(self.__data[i - 1]):
                    return False

                for j in range(i+1, self.__rows):
                    if self.__data[j][position] != 0:
                        return False
        
        return True

    '''
        Determine whether the matrix is in reduced row-echelon form

        Returns:
        bool -- the truth value of this test
    '''
    def is_in_reduced_row_echelon_form(self):
        if not self.is_in_echelon_form():
            return False

        for i in range(self.__rows):
            position = self.get_position_of_first_non_zero_of_row(self.__data[i])

            if self.__data[i][position] != 1:
                return False

            # the extra requirement that this matrix has to pass to be
            # regarded as being in reduced row-echelon form is to
            # have both positions above and below the position of the first
            # 1 in each row to have 0 as an element   
            position = self.get_position_of_first_non_zero_of_row(self.__data[i])

            for j in range(self.__rows):
                if j != i and self.__data[j][position] != 0:
                    return False
        
        return True
    
    '''
        Swap two rows in the matrix

        Keyword arguments:
        i -- index of the first row
        j -- index of the second row
    '''
    def swap_rows(self, i, j):
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]
    
    '''
        Get the transpose of the matrix

        Returns:
        matrix: the transpose of the matrix
    '''
    def transpose(self):

        sample_matrix = self.__get_sample_matrix(self.__columns, self.__rows)
        matrix = Matrix(data=sample_matrix)

        for i in range(self.__rows):
            for j in range(self.__columns):
                matrix.__data[j][i] = self.__data[i][j]
        
        return matrix

    '''
        Get a sample matrix

        Keyword arguments:
        rows -- the number of rows of the sample matrix
        columns -- the number of columns of the sample matrix
    '''
    def __get_sample_matrix(self, rows, columns):

        column_data = []
        i = 0
        while i < columns:
            column_data.append(None)
            i += 1

        row_data = []
        for i in range(rows):
            row_data.append(column_data)

        return row_data

    '''
        Add this matrix to a given matrix

        Keyword arguments:
        matrix_b -- the matrix to add to this matrix

        Returns:
        matrix -- the sum of the two matrices
    '''
    def add(self, matrix_b):
        matrix_a = self

        if not matrix_a.is_equal_to(matrix=matrix_b):
            raise RuntimeError('Matrix dimensions are not equal')

        sample_matrix = self.__get_sample_matrix(self.__rows, self.__columns)
        sum_matrices = Matrix(data=sample_matrix)

        for i in range(self.__rows):
            for j in range(self.__columns):
                sum_matrices.__data[i][j] = matrix_a.__data[i][j] + matrix_b.get_data[i][j]
        
        return sum_matrices

    '''
        Subtract a given matrix from this matrix

        Keyword arguments:
        matrix_b -- the matrix to subtract

        Returns:
        matrix -- the resultant matrix
    '''
    def subtract(self, matrix_b):
        matrix_a = self

        if matrix_b.num_rows() != matrix_a.__rows or \
                matrix_b.num_columns != matrix_a.__columns:

            raise RuntimeError("Matrix dimensions are not equal")

        sample_matrix = self.__get_sample_matrix(self.__rows, self.__columns)
        resultant_matrix = Matrix(data=sample_matrix)

        for i in range(matrix_a.__rows):
            for j in range(matrix_a.__columns):
                resultant_matrix.__data[i][j] = matrix_a.__data[i][j] - matrix_b.get_data()[i][j]
        
        return resultant_matrix
