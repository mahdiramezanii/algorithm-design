import numpy

def get_info():

    n=int(input("Enter N: "))
    m=int(input("Enter M: "))
    weight=[]
    value=[]
    array=numpy.random.randint(0,1,size=(n+1,m+1))

    for i in range(n+1):

        
        weight.append(int(input(f"Enter weight {i}: ")))
        value.append(int(input(f"Enter value {i}: ")))
            
    result=[n,m,weight,value,array]  

    return result      

def algoritm(n,m,weight,value,array):

    array=numpy.random.randint(0,1,size=(n+1,m+1))

    for i in range(n+1):

        for j in range(m+1):

            if ((i==0) or (j==0)):

                array[i][j]=0

            elif (weight[i] <= j ):

                array[i][j]=max(value[i]+array[i-1][j-weight[i]] , array[i-1][j])

            else:

                array[i][j]=array[i-1][j]

    i=n
    j=m

    while (i>0 or j>0):

        if (array[i][j] == array[i-1][j]):

            print(f"{i} is not use!")
            i=i-1
        else:

            print(f"{i} is use")
            j=j-weight[i]
            i=i-1

# n=4
# m=8
# weight=[0,2,3,4,5]
# value=[0,1,2,5,6]

# array=numpy.random.randint(0,1,size=(n+1,m+1))

# for i in range(n+1):

#     for j in range(m+1):

#         if ((i==0) or (j==0)):

#             array[i][j]=0

#         elif (weight[i] <= j ):

#             array[i][j]=max(value[i]+array[i-1][j-weight[i]] , array[i-1][j])

#         else:

#             array[i][j]=array[i-1][j]

# i=n
# j=m

# while (i>0 or j>0):

#     if (array[i][j] == array[i-1][j]):

#         print(f"{i} is not use!")
#         i=i-1
#     else:

#         print(f"{i} is use")
#         j=j-weight[i]
#         i=i-1
        
if __name__ == "__main__":

    information=get_info()
    algoritm(information[0],information[1],information[2],information[3],information[4])
