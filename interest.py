#function to return the compound interest
def  compound_interest(principal,rate,time):
    ci=principal*(pow((1+rate/100),time))
    print("compound interest :" ci)
    
compound_interest(10000 ,4,3)