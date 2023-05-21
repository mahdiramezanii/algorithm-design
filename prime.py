
    
def get_information():


    input_Gragh={}
    result={}

    flag=True

    while (flag):

        result.clear()
    
        top=input('Enter top: ')
        if top=="0":
            flag=False
            break
        n=int(input("Enter N: "))
    
        for i in range(n):
        
            widget=int(input("Enter Vazn: "))
            mane=input("Enter mane: ")
            result[widget]=mane

        test=result.copy()

        input_Gragh[top]=test

        
geragh={
    "a":{4:"b",8:"h"},
    "b":{8:"c",4:"a",11:"h"},
    "h":{7:"i",1:"g"},
    "i":{2:"c",6:"g"},
    "c":{4:"f",7:"d"},
    "d":{9:"e",14:"f"},
    "f":{10:"e"}   
}


delete={}
lis=[]
for k,v in geragh.items():

    print(f"root:{k}")

    for y,r in v.items():

        
        lis.append(y)

    print(lis)
    print(min(lis))
    print(v[min(lis)])    
    lis.clear()