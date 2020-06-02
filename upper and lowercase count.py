x= input("count the upper and lower case letter in the text")
y=0
z=0
for i in x:
    if i.isupper():
        y=y+1
    elif i.islower():
        z=z+1
   
        
        print ("uppercase:",(y))
        print ("lowercase:",(z))
