import random

n=random.randint(1,6)
attempt=0
while (n<8):
 gas=int(input("guess the number"))
 attempt+=1
 if n==gas:
     print( n," congrats your attempt",attempt)
     break
 else:
     print("sorry")
    
print("game end")
   
