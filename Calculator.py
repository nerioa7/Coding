def add(x,y):
    return x + y
    
def subtract (x, y):
    return x - y
    
def divide(x,y):
    return x / y
    
def multiply (x,y):
    return x * y
print (".................Pthon Calculator.................      ")

print ("1-> Add")
print ("2-> Minus")
print ("3-> Divide")
print ("4-> Multiplication")

while True:
    
    option = input("Enter a pick (1,2,3,4) \n")
    
    if option in ("1", "2" , "3", "4" ):
        num1 = int(input("Enter a Number"))
        num2 = int(input("Enter a Number"))
        
    if option == "1":
        print (num1, "+" ,num2, "=", add(num1, num2))
        
    elif option == "2":
        print ( num1 , "-" , num2, "=", subtract(num1, num2))
    
    elif option == "3":
        print ( num1 , "/" , num2, "=", divide(num1, num2))
        
    elif option == "4":
        print ( num1 , "*" , num2, "=", multiply(num1, num2))
        break
    else:
        print ("Please Enter a Number to calculate ")
    
    
    

