import  string
import  random
choice=input("Enter  your  choice  (odd/even):  ")
while(choice!="odd"  and  choice!="even"):
    print("invalid")
    choice=input("Enter  your  choice  (odd/even):  ")
a=int(input("  enter  a  random  number  between  1-6:  "))
#incase wrong-entry
while(a>=7):
    print("invalid  no.")
    a=int(input("  enter  a  random  number  between  1-6:  "))
b=random.randint(1,6)
print(f"computer choice {b}")
S=a+b
if(S%2==0 and  choice=="even"):
  toss=input("congrats  you  won  the  toss  \n  what  are  you  choosing  (batting/bowling)??:    ")
  print(f"You  are {toss} first!")
elif(S%2!=0 and  choice=="odd"):
  toss=input("congrats  you  won  the  toss  \n  what  are  you  choosing  (batting/bowling)??:    ")
  print(f"You   are {toss} first!")
else:
  print("you  lost  the  toss")
  cric=["batting","bowling"]
  soos=random.choice(cric)
  print(f"The  computer  has  chose  to  {soos}")
  SUM=0
for  i  in  range(0,11,1):
  j=int(input("enter  run:  "))
  c=random.randint(1,6)
  print(f"computer  put{c}")
  if(j==c  and  i==0):
    print("golden  duck")
    break
  elif(j==c):
    print(f"your  score  is  {SUM}")
    break
  else:
    SUM+=j
