sal=int(input("Enter salary earned per anum: "))
yrs=int(input("Enter the number of years worked: "))
if(yrs>10):
    bonus=0.8*sal
    print("bonus earned: " + bonus)
elif(yrs>=6) and (yrs<=10):
         bonus=0.08*sal
         print("bonus earned: " +bonus)
elif(yrs6):
           bonus=0.05*sal
           print("bonus earned: " + bonus)
else:
       print("invalid amount")
    