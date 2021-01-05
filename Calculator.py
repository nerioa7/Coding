//defining the add for x,y, which returns the value x,y
def add(x,y):
    return x + y

//defining the subtract for x,y, which returns the value x,y
def subtract (x, y):
    return x - y

//defining the divide for x,y, which returns the value x,y
def divide(x,y):
    return x / y

//defining the multiply for x,y, which returns the value x,y
def multiply (x,y):
    return x * y
print (".................Pthon Calculator.................      ")

print ("1-> Add")
print ("2-> Minus")
print ("3-> Divide")
print ("4-> Multiplication")

//while loop only execute if the condition is true
while True:

    //here is the option for the user to select the choosing of operator 
    option = input("Enter a pick (1,2,3,4) \n")
    
    if option in ("1", "2" , "3", "4" ):
      //user input of their own choice
        num1 = int(input("Enter a Number"))
        num2 = int(input("Enter a Number"))
        
        // if condition 
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
    
    
    

