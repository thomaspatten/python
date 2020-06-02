multiples=[]
for i in range (2000,3201):
    if (i%7==0) and (i%5>=1):
        multiples.append(str(i))
       
        

print(multiples)
