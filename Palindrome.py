############ wap tp check palindrome of  given string #########

str=(input("enter the string as u want = "))
org_str=""
for i in str:
    org_str=i+org_str
 
if(org_str==str):
    print("is palindrome")
else:
    print("not")    