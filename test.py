# first_num = int (input("Enter first number: "))
# second_num = int (input("Enter second number: "))
# while first_num <= second_num:
#     print(first_num)
#     first_num += 1
# print("Done")

# # Will be runnung continously
# while True:
#     first_num1 = int(input("Enter first number: "))
#     second_num2 = int(input("Enter second number: "))
#     if first_num1 > second_num2:
#         print("First number can not be bigger than second number")
#         continue
#     while first_num1 <= second_num2:
#         print(first_num1)
#         first_num1 += 1
#     print("Done")
#     if str(first_num1).lower() == "x" or str(second_num2).lower() == "x":
#         break

while True:
    try:
        first_input = input("Enter first number (or 'x' to exit): ")
        if first_input.lower() == 'x':
            break
        first_num1 = int(first_input)

        second_input = input("Enter second number (or 'x' to exit): ")
        if second_input.lower() == 'x':
            break
        second_num2 = int(second_input)
    except ValueError:
        print("Invalid input. Please enter integers or 'x' to exit.")
        continue

    if first_num1 > second_num2:
        print("First number cannot be bigger than second number")
        continue

    while first_num1 <= second_num2:
        print(first_num1)
        first_num1 += 1
    print("Done")