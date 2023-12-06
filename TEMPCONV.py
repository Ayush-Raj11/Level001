########### PROGRAM TO CONVERT TEMP AS USER WANT ( CELCIUS TO FAHRENHEIT OR FAHRENHEIT TO CELCIUS)  ########## 

def c_to_f(org_temp):
    ftemp=((org_temp*9/5)+32)
    return float(ftemp)

def f_to_c(org_temp):
    ctemp=((org_temp-32)*5/9)
    return float(ctemp)

org_temp=float(input("Enter the temp u want:"))
unit=input("Enter the unit of measurement (type c for celcius & f for fahrenheit ):")
temp_f=c_to_f(org_temp)
temp_c=f_to_c(org_temp)

if(unit=="c" or unit=="C"):
    print("Temp in fahrenheit :",temp_f)
elif(unit=="f" or unit=="F"):
    print("Temp in celcius:",temp_c)
else:
    print("Invalid input !! ,please put valid input as above format given")


    

    






