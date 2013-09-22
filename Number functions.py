def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def subtract(x,y):
    return x - y

def apply(func, x, y):
    return func(x, y)

def main():
    No1 = 0
    No2 = 0
    runAgain = True
    while runAgain == True:
        
        function = " "
        function = raw_input("Add, subtract, multiply, or divide? Enter A, S, M, or D.")
        No1 = float(raw_input("Enter the first number to work with:"))  
        No2 = float(raw_input("Enter the second number to work with:"))
        func = None
        if function == 'A':
            func = add
            
        elif function == 'S':
            func = subtract
            
        elif function == 'M':
            func = multiply
            
        elif function == 'D':
            func = divide
           
        else:
            print("The function you entered was invalid. Please try again.")
            main()  
        if func is not None:
            answer = apply(func, No1, No2)
            print("The answer is " + str(answer))
            runAgainIn = raw_input("Run again? True / False.")
            if runAgainIn == "True" or runAgainIn == "true":
                runAgain = True
            else:
                runAgain = False
    
main()


