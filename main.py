print("Welcome to Calculator")

num_one = input("Enter first number: ")
num_two = input("Enter second number: ")
operator = input("Enter an operator(+,-,/,x): ")

while (not num_one.isnumeric()) or (not num_two.isnumeric()):
    if(not num_one.isnumeric()):
        num_one = input("Integers are only allowed! Please enter an integer for the first number: ")
    if(not num_two.isnumeric()):
        num_two = input("Integers are allowed! Please enter an integer for the second number: ")

num_one = int(num_one)
num_two = int(num_two)

match operator:
    case "+":
        print(num_one, "+" ,num_two , " = ",num_one + num_two)
    case "-":
        print(num_one, "-" ,num_two , " = ",num_one - num_two)
    case "/":
        print(num_one, "/" ,num_two , " = ", num_one / num_two)
    case "x":
        print(num_one, "x" ,num_two , " = ",num_one * num_two)