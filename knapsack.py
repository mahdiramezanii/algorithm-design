import numpy
n=4
m=8
weight=[0,2,3,4,5]
value=[0,1,2,5,6]

array=numpy.random.randint(0,1,size=(n+1,m+1))

for i in range(n+1):

    for j in range(m+1):

        if ((i==0) or (j==0)):

            array[i][j]=0

        elif (weight[i] <= j ):

            array[i][j]=max(value[i]+array[i-1][j-weight[i]] , array[i-1][j])

        else:

            array[i][j]=array[i-1][j]



print(array[n][m])