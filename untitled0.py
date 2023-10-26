import random
mylist = ["rock","paper","scissors"]
y=random.randint(0,len(mylist)-1)

mylist = ["rock","paper","scissors"]
print("değer gir :")
f=input()
f=int(f)
print(y)

if f==y:
    print('tie')
elif f==0:
    if y==1:
        print("pc beat 01")
    else:
        print("you beat 02")
elif f==1:
    if y==0:
        print("you beat 10")
    else:
        print("pc beat 12")
elif f==2:
    if y==0:
        print("pc beat 20")
    else:
        print("you beat 21")
else:
    print("only 0,1,2")