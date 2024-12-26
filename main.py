print("Welcome to Calculator")

num_one = int(input("Input first number: "))
num_two = int(input("Input second number: "))
operator = input("Input an operator(+,-,/,x): ")

match operator:
    case "+":
        print(num_one, "+" ,num_two , " = ",num_one + num_two)
    case "-":
        print(num_one, "-" ,num_two , " = ",num_one - num_two)
    case "/":
        print(num_one, "/" ,num_two , " = ", num_one / num_two)
    case "x":
        print(num_one, "x" ,num_two , " = ",num_one * num_two)