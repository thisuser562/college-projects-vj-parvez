import  string
import  random
choise=input("Enter  your  choice  (odd/even)")
a=int(input("  enter  a  random  number  between  1-6"))
b=random.randint(1,6)
S=a+b
if(S%2==0 and  choice=="even"):
  print("congrats  you  won  the  toss  \n  what  are  you  choosing  (batting/bowling)??")
elif(S%2!=0 and  choice=="odd"):
  print("congrats  you  won  the  toss  \n  what  are  you  choosing  (batting/bowling)??")
else:
  print("you  lost  the  toss")
  cric=["batting","bowling"]
  soos=random.choice(cric)
  print(f"The  computer  has  chose  to  {soos}")

 
  
  
