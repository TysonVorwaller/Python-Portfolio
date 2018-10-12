#Tyson Vorwaller
#Period 4-5
#10/12/18
#Combat System
import random
  
win=0 
pHP = 100
mHP = 1000
print("You are King Arthur and is now faced against an horde of deadly rabbits.")
choice = input("fight or run")

while choice == "fight":
    playerDamage = random.randrange(0,31)
    print("you attack the rabbits and did",playerDamage,"damage.")
    mHP -= playerDamage
    if mHP > 0:
        monsterDamage = random.randrange(0,51)
        print("the rabbits fight back doing ",monsterDamage,"damage.")
        pHP -= monsterDamage
    if pHP <=0:
        print("you have died")
        win = 0
        break
    elif mHP <= 0:
        print ("You have slain the rabbits you didn't even need the holy hand grenade that time.")
        win = 1
        break
    elif pHP >=0 and mHP >= 0:
        print("you have",pHP,"health")
        print("the rabbits have",mHP,"health")
        choice = input("fight or run")
        if choice == "fight":
            print("you attack again")
        if choice == "run":
            break

if choice == "run":
    print("Oi there ya big ninny!")
if win == 0:
    print("The rabbits overtake you and devour the flesh off your bones")
else:
        print ("You have slain the rabbits you didn't even need the holy hand grenade that time.")










        
