#Just type your limit here
limit = 20

limit -= 1

times = 0

print("1! = 1")
print("2! = 2")

def factorial(num, num2):

  

  while num2 > 1:
      
    fact = num * num2

    num2 -= 1

    num = fact
    
  print(str(print_time) + "! = " + str(num))


patern = 3
    
print_time = 3

if limit != 1:
  factorial(patern, patern - 1)
  times += 1
  print_time += 1

while times != limit - 1:
  patern += 1
  factorial(patern, patern - 1)
  times += 1
  print_time += 1