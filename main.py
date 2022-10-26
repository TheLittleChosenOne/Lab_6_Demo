
first_num = float(input("Enter first operand: "))
second_num = float(input("Enter second operand: "))

print("Calculator Menu\n"
          "---------------\n"
          "1. Addition\n"
          "2. Subtraction\n"
            )


operation_num = int(input("Which operation do you want to perform? "))

if (operation_num == 1):
    result = (first_num + second_num)

elif (operation_num == 2):
    result = (first_num - second_num)

else:
    print("Error: Invalid selection! Terminating program.")

print(f"The result of the operation is  { result } . Goodbye!")




