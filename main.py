operators = ["+", "-", "/", "x", "*"]
print("Welcome to Calculator")

def mainMenu():
    print("\nMain menu.")
    print("1. Insert two numbers and operator.")
    print("2. Insert an expression.") # TODO    
    print("3. Exit.")

def validExpression(expression):
    stack = []
    for i in expression:
        if (i == "(") or (i == "{") or (i == "["):
            stack.append(i)
        elif i == (")" or "}" or "]") and (len(stack) == 0):
            return False    
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
    return len(stack) == 0

# def solveExpression(expression):
#     i = 0
#     j = 0
#     while i < len(operators):
#         if len(expression.split(operators[i])) > 1:
#             break
#         i+=1

#     print(operators[i], " dsfsf s", expression.split())

userOption = 0

while userOption >= 0:
    mainMenu()
    userOption = input("\nOption: ")

    while (not userOption.isnumeric()) or (not (0 <= int(userOption) <= 3)):    
        if not userOption.isnumeric():
                userOption = input("You didn't input an number, please select one: ")
        if not 0 <= int(userOption) <= 3:
                userOption = input("You selected a number, but not one of the options. Please select one of the options: ")

    userOption = int(userOption)


    if (userOption == 1):
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

        print("\n")

        match operator:
            case "+":
                print(num_one, "+" ,num_two , " = ",num_one + num_two)
            case "-":
                print(num_one, "-" ,num_two , " = ",num_one - num_two)
            case "/":
                if num_two == 0:
                    print("Can't divide by zero, champ.")
                else:
                    print(num_one, "/" ,num_two , " = ", num_one / num_two)
            case "x":
                print(num_one, "x" ,num_two , " = ",num_one * num_two)
            case "*":
                print(num_one, "x" ,num_two , " = ",num_one * num_two)
    elif userOption == 3:
        print("GoodBye.")
        break
    else:
        userExpression = input("Insert expression: ")

        leftSide = userExpression.split("=")[0].replace(" ", "")
        rightSide = userExpression.split("=")[1].replace(" ", "")
        
        print(True == (validExpression(leftSide) and validExpression(rightSide)))
        # print(validExpression(userExpression))

        # solveExpression(leftSide)
        # print()
        # print()
        # solveExpression(rightSide)