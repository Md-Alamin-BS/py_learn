from math import *

def check(num):
    return print(f"Yes, {num} is in the list") if num in [1, 2, 3, 4, 5] else print(f"{num} is not in the list")

if __name__ == "__main__":
    print("Hello, World!")
    for i in range(1, 6):
        print(' ' * (5 - i) + '*' * (2 * i - 1))

    test_str="Hello, Python!"
    print (len(test_str))
    print (test_str[0])
    print (test_str.index('P'))
    print (test_str.count('o', 7, 14)) #string.count(value, start, end)
    print (test_str.find('python')) #gives -1 if value not found, same as index but does not throw exception
    print (test_str.replace('Python', 'World', 0)) #string.replace(oldvalue, newvalue, count) -count how mnay times to replace

    test_num = 1234
    print (str(test_num) + " is a number")
    print(abs(-1))
    print(pow(2, 3))
    print(max(1, 2, 3, 4))
    print(min(1, 2, 3, 4))
    print(round(3.14159, 2))
    print(floor(-3.9)) 
    print(ceil(3.1))
    print(sqrt(16))

    # name = input("Enter your name: ") #input() waits for user input
    # age = input("Enter your age: ")
    # print ("Hello, " + name + "! " "You are " + age + " years old.")
    # num1 = input("Enter a number: ")
    # num2 = input("Enter a number: ")
    # result = float(num1) + float(num2)
    # print(result)

    Tests = ["Black box", "White box", "Gray box", "Unit", "Integration", "System", "Acceptance"]
    Tests[1] = "Clear box"
    print(Tests[1])
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.extend(Tests)
    numbers.insert(6, 7)
    print(numbers)
    Tests.remove("Clear box")
    Tests.insert(1, "Regression")
    # Tests.extend(numbers)
    # Tests.pop(19)
    # print(Tests) 
    # # Tests.clear()
    # print(Tests)
    # print(numbers.index(7))
    Tests.sort()
    print(Tests)
    Tests.reverse()
    print(Tests)    

    # def max_num(num1, num2, num3):
    #     if num1>=num2 and num1>=num3:
    #         return num1
    #     elif num2>=num1 and num2>=num3:
    #         return num2
    #     else:
    #         return num3
    
    # input1 = float(input("Enter a number: "))  
    # input2 = float(input("Enter second number: "))  
    # input3 = float(input("Enter third number: "))

    # print(max_num(input1, input2, input3))


    # while True:
    #     try:
    #         num1 = float(input("Enter a number: "))
    #         break
    #     except ValueError:
    #         print("Invalid input. Please enter a valid number.")

    # valid_operators = ["+", "-", "/", "*"]
    # op = input("Enter operator: ")
    # while op not in valid_operators:
    #     print("Invalid operator. Please enter one of the following: +, -, /, *")
    #     op = input("Enter operator: ")

    # while True:
    #     try:
    #         num2 = float(input("Enter second number: "))
    #         break
    #     except ValueError:
    #         print("Invalid input. Please enter a valid number.")

    # if op == "+":
    #     print(f"The result of ({num1} + {num2}) is {num1 + num2}")
    # elif op == "-":
    #     print(f"The result of ({num1} - {num2}) is {num1 - num2}")
    # elif op == "/":
    #     print(f"The result of ({num1} / {num2}) is {num1 / num2}")
    # elif op == "*":
    #     print(f"The result of ({num1} * {num2}) is {num1 * num2}")
    # else:
    #     print("Invalid operator, only +, -, /, * are allowed")

    num = int(input("Enter a number: "))
    check(num)

