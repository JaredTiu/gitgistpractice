first_input = float(input("Input first number: "))
second_input = float(input("Input second number: "))

if first_input != second_input:
    print("Numbers are not equal, printing the biggest and lowest.")
    if first_input > second_input:
        print("The biggest number is:", first_input)
        print("The lowest number is:", second_input)
    elif second_input > first_input:
        print("The biggest number is:", second_input)
        print("The lowest number is:", first_input)
elif first_input == second_input: 
    print("Numbers are equal")