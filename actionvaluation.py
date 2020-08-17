#y = a + b*x

print("Hi! This program is going to help you figure out the final value of your(s) action(s) ")

a = float(input("\nPlease insert the first variable: "))

b = float(input("\nPlease insert the second variable: "))

x = float(input("\nInsert the inicial value of your action: "))

y = a + b*x



just_once = input("\nDo you want to know the value of your action multiplied for more times? [y] [n]\nAnswer here: ")

if just_once == "n":
  print("\nThe final value of your action is " + str(y) + "$")
   

elif just_once == "y":
  how_many_times = int(input("\nType the amount of times you want to calculate your action value (you will be able to change the variable values if you want to): "))


  
  variables_change = input("\nDo you want to change the value of your variables at some point? [y] [n]\nAnswer here: ")
  if variables_change == "y":

    print("\nThe final value of your action is " + str(y)+ "$")
    for index in range(how_many_times - 1):
      variables_change = input("\nDo you want to change the value of any of your variables for the next action? [y] [n]\nAnswer here: ")

      if variables_change == "y":
        a = float(input("\nPlease insert the first variable: "))

        b = float(input("\nPlease insert the second variable: "))

        x = y
        y = a + b*x
        print("\nThe final value of your action is " + str(y)
        + "$")
      if variables_change == "n":
          
        x = y
        y = a + b*x
        x = y
        print("\nThe final value of your action is " + str(y)
        + "$")
          
        
  elif variables_change == "n":
    print("\nThe final value of your action is " + str(y) + "$")
    for index in range(how_many_times - 1):
      x = y
      y = a + b*x
        
        

      print("\nThe final value of your action is " + str(y) + "$")

    

