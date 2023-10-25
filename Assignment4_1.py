import random

pc_number=random.randint(0,20)
count=0
while True:
    user_number=int(input("yek adad beyn 1 ta 20 vared konid :"))
    count+=1


    if user_number==pc_number:
        print("Ok")
        break
    elif user_number<pc_number:
         print("add bozorg tar vared kon")

    elif user_number>pc_number:
         print("adad kochek tari ra vared kon")
  

print("adade dar nazar gerfte shode tavasot Computer:",pc_number)
print("tedad hads haye karbar:",count)