import numpy

arr=numpy.chararray((4,4), itemsize=1, unicode=True, buffer=None, offset=0, strides=None, order=None)


def is_safe(array, row, col, n):
    

    for i in range(col):
        if array[row][i] == "Q":
            return False

    # قطری بالا
    i = row
    j = col
    while i >= 0 and j >= 0:
        if array[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # قطری پایین
    i = row
    j = col
    while i < n and j >= 0:
        if array[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True

#==================================================================================

def print_array(array):
    
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=" ")
            
        print("\n")

#======================================================================================



def solve_n_queens_util(array, col, n):
    # stop Condition
    if col >= n:
        return True

    
    for i in range(n):
        
        if is_safe(array, i, col, n):
            array[i][col] = "Q"

            
            if solve_n_queens_util(array, col + 1, n):
                return True


            array[i][col] = "-"

#=================================================================================================

def solve_n_queens(n):
    
    array = [["-" for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(array, 0, n):
        
        return False

    print_array(array)

#=================================================================================

solve_n_queens(4)
