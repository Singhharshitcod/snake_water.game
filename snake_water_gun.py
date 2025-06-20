import getpass
def win_func(p1,p2):
     #1,0,-1:snake,water,gun

     #player1 win
    if(p1==1 and p2==0): #player1:snake and player2:water
        print(f"Snake drinks Water → 🐍 beats 💧")
        return "p1" 
    if(p1==0 and p2==-1): #player1:water and player2:gun
        print(f"Water douses Gun → 💧 beats 🔫")
        return "p1"
    if(p1==-1 and p2==1):  #player1:gun and player2:snake
        print(f"Gun kills Snake → 🔫 beats 🐍")
        return "p1"
    
     #player2 win
    if(p2==1 and p1==0): #player2:snake and player1:water
        print(f"Snake drinks Water → 🐍 beats 💧")
        return "p2"
    if(p2==0 and p1==-1): #player2:water and player1:gun
        print(f"Water douses Gun → 💧 beats 🔫")
        return "p2"
    if(p2==-1 and p1==1): #player2:gun and player1:snake
        print(f"Gun kills Snake → 🔫 beats 🐍") 
        return "p2"
    
     #draw
    if(p1==p2): 
        print(f"Identical choices!🟰")
        return "dr"
round=1;  
p1count=0
p2count=0
name1=input("🧑 ENTER THE PLAYER1 NAME: ")
name2=input("👤 ENTER THE PLAYER2 NAME: ")
while(True):
    print(f"🎯 ROUND {round} 🎯")
    player1=getpass.getpass(f"🧑 {name1}: 🎮 CHOOSE - [🐍 Snake (s) / 🔫 Gun (g) / 💧 Water (w)] : ")   
    player2=getpass.getpass(f"👤 {name2}: 🎮 CHOOSE - [🐍 Snake (s) / 🔫 Gun (g) / 💧 Water (w)] : ")
    valid_choices = ['s', 'w', 'g']
    if player1 not in valid_choices or player2 not in valid_choices:
       print("Invalid input! Please choose only s (snake), w (water), g (gun).")
       print()
       continue
    pl1=0;
    pl2=0;
    if(player1=="s"):
        pl1=1
    if(player1=="w"):
        pl1=0
    if(player1=="g"):
        pl1=-1    

    if(player2=="s"):
        pl2=1
    if(player2=="w"):
        pl2=0
    if(player2=="g"):
        pl2=-1    
    win=win_func(pl1,pl2)   
    if(win=="p1"):
        print(f"🧑{name1} WIN THIS ROUND 🎉")
        p1count=p1count+1   
    if(win=="p2"):
        print(f"👤{name2} WIN THIS ROUND🎉")
        p2count=p2count+1   
    if(win=="dr"):
         print(f"THIS ROUND IS DRAW 🟰")
    print()
    if(p1count==5 or p2count==5):
        if(p1count==5):
            print(f"🏆 WINNER OF THIS GAME IS: 🧑 {name1}  🎉🎉🎉")
            print(f"📊 SCOREBOARD OF THIS GAME: 🧑 {name1} : {p1count} POINT ,👤 {name2} : {p2count} POINT")
            print()
            break
        if(p2count==5):
            print(f"🏆 WINNER OF THIS GAME IS: 👤 {name2}  🎉🎉🎉")
            print(f"📊 SCOREBOARD OF THIS GAME: 🧑 {name1} : {p1count} POINT ,👤 {name2} : {p2count} POINT")
            print()
            break
    round=round+1
    
