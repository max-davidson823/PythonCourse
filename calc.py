equation = input('Please enter equation ("x + y"): ').split(" ")
    
if len(equation) != 3:
    print("Invalid equation")
    exit()

num1 = equation[0]
num2 = equation[2]

if not num1.isdigit() or not num2.isdigit():
    print("Invalid numbers")
    exit()
    
num1 = int(num1)
num2 = int(num2)

if equation[1] not in ['+', '-', '*', '/']:
    print('Invalid operation')
    exit()

operation = equation[1]

match operation:
    case '+':
        sum = num1 + num2
        print(sum)
    case '-':
        difference = num1 - num2
        print(difference)
    case '*':
        product = num1 * num2
        print(product)
    case '/':
        if num2 == 0:
            print('Division by zero is not allowed')
            exit()
        quotient = num1 / num2
        print(quotient)
    case _:
        print('Invalid operation')