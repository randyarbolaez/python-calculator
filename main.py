print("Welcome to Calculator. Main Menu")

def mainMenu():
    print("1. Insert two numbers and operator.")
    print("2. Insert an expression.") # TODO    

mainMenu()

userOption = input("Option: ")

if (userOption == "1"):
    operators = ["+", "-", "/", "x", "*"]
    num_one = input("Enter first number: ")
    num_two = input("Enter second number: ")
    operator = input("Enter an operator(+,-,/,x,*): ")

    while (not num_one.isnumeric()) or (not num_two.isnumeric()) or (not operator in operators):
        if(not num_one.isnumeric()):
            num_one = input("The first number isn't an number, please enter an integer for the first number: ")
        if(not num_two.isnumeric()):
            num_two = input("The second number isn't an number, please enter an integer for the second number: ")
        if(not operator in operators):
            operator = input("The operator doesn't make sense, please select one(+,-,/,x,*) : ")

    num_one = int(num_one)
    num_two = int(num_two)

    match operator:
        case "+":
            print(num_one, "+" ,num_two , " = ",num_one + num_two)
        case "-":
            print(num_one, "-" ,num_two , " = ",num_one - num_two)
        case "/":
            if num_two is 0:
                print("Can't divide by zero, champ.")
            else:
                print(num_one, "/" ,num_two , " = ", num_one / num_two)
        case "x":
            print(num_one, "x" ,num_two , " = ",num_one * num_two)
        case "*":
            print(num_one, "x" ,num_two , " = ",num_one * num_two)
else:
    print("Feature not yet available.")