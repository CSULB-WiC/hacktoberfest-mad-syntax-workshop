from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
Computer = t[randint(0,2)]

#set player to False
player = false

while player == false:
#set player to True
    player = input("Rock, Paper, Scissors?\n")
  
    if player == computer:
        print("/nTie!")
        print("Type Exit to end game./n")
      
    elif player == "Rock"
        if computer == "Paper"
            print("\nYou lose!", computer, "covers", player)
            print("Type Exit to end game.\n")         
        else:
            print("\nYou win!", player, "smashes", computer)
            print("Type Exit to end game.\n")
          
    elif player == "Paper":
        if computer == "Scissors":
            print("\nYou lose!", computer, "cut", player
            print("Type Exit to end game.\n"
        else:
            print("\nYou win!", player, "covers", computer)
            print("Type Exit to end game.\n")
          
  elif player == "Scissors"
        if computer == "Rock":
            print("\nYou lose...", computer, "smashes", player)
            print("Type Exit to end game.\n")          
        else:
            print("\nYou win!", player, "cut", computer)
            print("Type Exit to end game.\n")
          
    elif player == "Exit":
      print("\nExiting ...")
      quit(0)
    else:
        print("\nThat's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = false
    computer = t[randint(0,2)]
  
# Code Source : https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/