import numpy

arr=numpy.chararray((4,4), itemsize=1, unicode=True, buffer=None, offset=0, strides=None, order=None)


for i in range(4):

    for j in range(4):


        arr[i][j]="-"
        
        

        
def print_array(array):


    print(array)


def is_safe(array,row,col):


    for i in range(col):


        if array[row][i]=="Q":
            print("YESS")
          
            return False
        
   


    for i in range(row):
        
        if array[i][col]=="Q":
            print("NOOOO")
            

            return False 

     


    for i in range(row,4):

        for j in range(col,4):


            if (i == j):
                
               
                if array[i][j]=="Q":
                   
                    return False
    

    for i in range(-row,-1,1):

        for j in range(-col,-1,1):


            if (i == j):
                
               
                if array[i][j]=="Q":
                   
                    return False
                
    for i in range(3,row-2,-1):

        for j in range(3,col-2,-1):


            if (i == j):
                print("HHHH")
                print(i,j)
               
                if array[i][j]=="Q":
                   
                    return False

    return True    


def solve(array):

    for i in range(4):

        for j in range(4):

            
            if is_safe(array,i,j):

                
                array[i][j]="Q"

    print(array)
        

solve(arr)

