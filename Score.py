unit1=int(input("Enter marks for unit 1: "))
unit2=int(input("Enter marks for unit 2: "))
unit3=int(input("Enter marks for unit 3: "))
average=(unit1+unit2+unit3)/3
if(average>=70)and (average<=100):
    print("A")
elif(average>=60)and(average<=69):
    print("B")
elif(average>=50)and(average<=59):
    print("C")
elif(average>=40)and(average<=49):
    print("D")
else:
    print("FAIL")
