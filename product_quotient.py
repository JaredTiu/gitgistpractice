def remove_point_zero(number):
    if number % 1 == 0:
        return int(number)
    else:
        return number

first_input = float(input("Input first number: "))
second_input = float(input("Input second number: "))
product_of_inputs = remove_point_zero(first_input * second_input)
quotient_of_inputs = remove_point_zero(first_input / second_input)

product_or_quotient = int(input("Do you want the difference or sum of the numbers?(type 1 for product 2 for quotient): "))
if product_or_quotient == 1: 
    print(product_of_inputs)
elif product_or_quotient == 2: 
    print(quotient_of_inputs)