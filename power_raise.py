def remove_point_zero(number):
    if number % 1 == 0:
        return int(number)
    else:
        return number

first_input = float(input("Input first number: "))
second_input = int(input("Input what number you want to raise it to: "))

raised_of_inputs = remove_point_zero(first_input ** second_input)

print(raised_of_inputs)