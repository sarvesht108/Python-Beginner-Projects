a=int(input("Enter first number= "))
b=int(input("Enter sevind number= "))
print("1.Addition")
print("2.substraction")
print("3.multiplcation")
print("4.division")
choose=int(input("Enter your choose= "))
if(choose==1):
    print("resul: ", a+b)
elif(choose==2):
        print("result: ", a-b)
elif(choose==3):
            print("result: ", a*b)
elif(choose==4):
              print("result: ", a/b)
else:
              print("invalid input")              
              