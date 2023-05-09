import numpy

n=5
m=30 #وزن کوله پشتی

weight=[8,6,10,3,15]
value=[12,18,5,15,30]
final_value=0
sum_weight=0
result={}

array=numpy.random.randint(0,1,size=(n,3))

# for i in range(n):

#     for j in range(3):

#         if (j==0):

#             array[i][j]=i+1

#         elif (j==1):

#             array[i][j]=value[i]

#         elif (j==2):
#             array[i][j]=weight[i]

#division value / weight
for i in range(n):

    result[i+1]=value[i]/weight[i] 

#=============================================== sort dict =================================
sorted_footballers_by_goals = sorted(result.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_footballers_by_goals)
print(converted_dict)
#===============================================


for k,v in converted_dict.items():

    
    if (weight[k-1] + sum_weight <= m):

        final_value+=value[k-1]
 
        sum_weight+=weight[k-1]
       

    elif (weight[k-1] + sum_weight > m ):
   
        a= m - sum_weight

        if a>0:
    
            final_value+=(a / weight[k-1]) * value[k-1]
            sum_weight+=weight[k-1]

print(final_value)
