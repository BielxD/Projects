# E = m*c²

m = float(input("Please insert mass: "))

value = input("\nIs there a value to 'm' be mutiplied for? [y][n]: ")

if value == "n":
  pass

if value == "y":
  multiply = float(input("\nPlease insert the value here: "))

value2 = input("\nDo you want to multiply it by something else? [y] [n]: ")

if value2 == "n":
  multiply * m

if value2 == "y":
  multiply2 = float(input("\nPlease insert the value here: "))
  multiply * multiply2 * m


c = 300.000

E = m * (c*c)

print("\nYour final result is " + str(E) + "J")