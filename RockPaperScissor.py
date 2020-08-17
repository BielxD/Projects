import random

#Explanation
print("Welcome to this Rock, Paper, Scissor game.\nThe machine it's gonna play against you, every round has three games, the game ends in three rounds.\nLet's get started!")



loop = True

#Game function
def play():

  name = input("\nHow do you wanna be called?\n\nAnswer here: ")

  player_points = 0
  player_rounds = 0

  robot_points = 0
  robot_rounds = 0
  
  rounds = 0

  while rounds < 3:

    decision = int(input("\n\n1 - Rock\n2 - Paper\n3 - Scissor\n\nType the number of the one that you'd like to pick: "))
  
    

    global loop

    if decision == 1:
      print("\nRock!")
      loop = False
    if decision == 2:
      print("\nPaper!")
      loop = False
    if decision == 3:
      print("\nScissor!")
      loop = False
  
    while loop == True: 
      decision = int(input("\nPlease, press a valid number.\nThe options are:\n\n1 - Rock\n2 - Paper\n3 - Scissor\n\nType the one that you'd like to pick: "))

      if decision == 1:
        print("\nRock!")
        loop = False
      if decision == 2:
        print("\nPaper!")
        loop = False
      if decision == 3:
        print("\nScissor!")
        loop = False
    robot_decision = random.randint(1, 3)
  
    if robot_decision == 1:
      print("\nVS\n\nRock!")
  
    if robot_decision == 2:
      print("\nVS\n\nPaper!")

    if robot_decision == 3:
      print("\nVS\n\nScissor!")
  
    if decision == robot_decision:
      print("\nThat's a tie, no points aren't gonna be processed!")

    elif decision == 1 and robot_decision == 2:
      print("\nRobot wins!")
      robot_points += 1

    elif decision == 2 and robot_decision == 3:
      print("\nRobot wins!")
      robot_points += 1

    elif decision == 3 and robot_decision == 1:
      print("\nRobot wins!")
      robot_points += 1

    elif decision == 2 and robot_decision == 1:
      print("\n" + name + " You win!")
      player_points += 1

    elif decision == 3 and robot_decision == 2:
      print("\n" + name + " You win!")
      player_points += 1

    elif decision == 1 and robot_decision == 3:
      print("\n" + name + " You win!")
      player_points += 1

    else:
      print("\nI'm sorry but if you type a wrong number the game is gonna start over")
      player_points = 0
      player_rounds = 0

      robot_points = 0
      robot_rounds = 0
  
      rounds = 0

    if player_points == 3:
      print("\n" + name + " you've win a round!")
      player_rounds += 1
      rounds += 1
      player_points = 0
      robot_points = 0
    if robot_points == 3:
      print("\nRobot has win a round!")
      robot_rounds += 1
      rounds += 1
      robot_points = 0
      player_points = 0

    print("Player = " + str(player_points) + " points and " + str(player_rounds) + " rounds" + "\nRobot = " + str(robot_points) + " points and " + str(robot_rounds) + " rounds")

    if rounds == 3:
      if player_rounds > robot_rounds:
        print("\nCongratulations " + name + " you've win the game!")
      if player_rounds < robot_rounds:
         print("\nThe robot has win!")

      play_again = str(input("\nDo you wanna play again? [y] [n]\nAnswer here: "))
    
      if play_again == "y":
        player_points = 0
        player_rounds = 0
        robot_points = 0
        robot_rounds = 0
        rounds = 0               
        print("Player = " + str(player_points) + " points and " + str(player_rounds) + " rounds" + "\nRobot = " + str(robot_points) + " points and " + str(robot_rounds) + " rounds")

      print("That's for playing :D")
      


play()



