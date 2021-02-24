#Calculator
from Calculator import art

#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Division
def divide(n1,n2):
    return n1 / n2

 #Multiply
def multiply(n1,n2):
    return n1 * n2


operations = {
    "+": add, 
    "-": subtract, 
    "/": divide, 
    "*": multiply
}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol) 

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continuation = input(f"Type y to continue calculating with {answer}, type new for a new calculation or type n to exit the calculator:" ).lower()
        if continuation == "y":
            num1 = answer
        elif continuation == "new":
            # Recursion: Calling a function within itself.
            calculator()
        else:
            print("Goodbye")
            should_continue = False


calculator()





