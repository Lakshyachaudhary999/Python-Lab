password="2003"
c=5
while c>0:
 a=input("enter password")
 if a==password:
  print("login successfull")
 else: 
   c=c-1
   print("wrong password")
   print(f"{c} attempts left")
   
