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

# while True:
#     try:
#         first_input = input("Enter first number (or 'x' to exit): ")
#         if first_input.lower() == 'x':
#             break
#         first_num1 = int(first_input)

#         second_input = input("Enter second number (or 'x' to exit): ")
#         if second_input.lower() == 'x':
#             break
#         second_num2 = int(second_input)
#     except ValueError:
#         print("Invalid input. Please enter integers or 'x' to exit.")
#         continue

#     if first_num1 > second_num2:
#         print("First number cannot be bigger than second number")
#         continue

#     while first_num1 <= second_num2:
#         print(first_num1)
#         first_num1 += 1
#     print("Done")


# secrect_word = "Python"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secrect_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of guesses, You lose!")
# else:
#     print("You win!")


# secrect_word = "Python"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secrect_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         if guess != secrect_word:
#             if guess_count + 1 < guess_limit:
#                 print("Wrong guess, try again.")
#         guess_count += 1
#     else: 
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of guesses, You lose!")
# else:
#     print("You win!")


# secret_word = "Python"
# guess = ""
# guess_count = 0
# guess_limit = 3

# while guess != secret_word and guess_count < guess_limit:
#     guess = input("Enter guess: ")
#     if guess != secret_word and guess_count + 1 < guess_limit: #guess_count + 1 < guess_limit is used to check if the user has one more guess left before printing the message to avoid printing the message when the user has no more guess left
#             print(f"Wrong guess, You have {guess_limit - guess_count - 1} more guess/es.")
#     guess_count += 1

# if guess == secret_word:
#     print("Correct guess, You win!")
# else:
#     print("Out of guesses, You lose!")


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print("\n")


for letter in "Python":
    print(letter)

for x in [0, 1, 2]:
    # print(x)
    pass

for x in range(6):
  if x == 3: 
    # break        # using break here will not execute the else block
    print(x)
else:
  print("Finally finished!")

  print (pow(2, 3)) # 2^3 = 8