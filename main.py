#printing the welcome message
print("Welcome to treasure Island ,Your mission is to find the treasure")

#asking the user to select "Right" or "Left"
choice1 = input("Select either left or right:")

#doing the if-else operation on the flowchart
if choice1 == "left" or choice1 =="LEFT":
   choice2 = input("You have come to a lake now you have to either select wait or swim").lower()
   if choice2 =="wait" :
       choice3 = input("Select the door either Red,Blue,Yellow")
       if choice3 == "Yellow" or choice3=="yellow":
           print("you win")
       elif choice3 == "Red" or choice3 =="red":
           print("Burned by fire ,Game over")
       elif choice3 == "Blue" or choice3 == "blue":
           print("Eaten by beast,Game over")
       else:
           print("Game over")
   else:
       print("Game over")
else:
    print("Your game is over")

