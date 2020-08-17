
def intire_num():

    num = float(input("Type a number in here: "))
    intire = False
    
    if num < 0:
        print("Error")
        intire = True
    
    elif num == 0:
        print("Intire number")
        intire = True
    
    elif num % 2 == 0:
        print("Intire number")
        intire = True
    
    elif (num + 1) % 2 == 0:
        print("Intire number")
        intire = True
    
    elif intire == False:
        print(str(num) + " is not an intire number")
        
intire_num()