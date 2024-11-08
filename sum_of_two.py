def remove_point_zero(number):
    if number % 1 == 0:
        return int(number)
    else:
        return number

first_input = float(input("Input first number: "))
second_input = float(input("Input second number: "))
sum_of_inputs = remove_point_zero(first_input + second_input)
diff_of_inputs = remove_point_zero(first_input - second_input)

sum_or_diff = int(input("Do you want the difference or sum of the numbers?(type 1 for sum 2 for diff): "))
if sum_or_diff == 1: 
    print(sum_of_inputs)
elif sum_or_diff ==2: 
    print(diff_of_inputs)