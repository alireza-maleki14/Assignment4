import random
tas=random.randint(1,6)
count=0
while True:

    count+=1
    if tas==1 or tas==2 or tas==3 or tas==4 or tas==5:
        print(tas)
        break
    elif tas==6:
        print("6")
        tas=random.randint(1,6)
     
    
print("tedad dafaat rikhtan tas:",count)
