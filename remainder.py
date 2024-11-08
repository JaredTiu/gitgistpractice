def remove_point_zero(number):
    if number % 1 == 0:
        return int(number)
    else:
        return number

first_input = float(input("Input first number: "))
second_input = float(input("Input second number: "))
remainder_of_inputs = remove_point_zero(first_input % second_input)

print(remainder_of_inputs)