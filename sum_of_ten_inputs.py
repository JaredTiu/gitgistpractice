first_input = int(input("Input a number: "))
second_input = int(input("Input a number: "))
third_input = int(input("Input a number: "))
fourth_input = int(input("Input a number: "))
fifth_input = int(input("Input a number: "))
sixth_input = int(input("Input a number: "))
seventh_input = int(input("Input a number: "))
eighth_input = int(input("Input a number: "))
nineth_input = int(input("Input a number: "))
tenth_input = int(input("Input a number: "))

number_list = [first_input, second_input, third_input, fourth_input, fifth_input, sixth_input, seventh_input, 
               eighth_input, nineth_input, tenth_input ]

sum_or_diff = int(input("Do you want the sum or difference?(type 1 for sum and 2 for diff): "))
if sum_or_diff == 1:
    print(sum(number_list))
elif sum_or_diff == 2: 
    number_difference = first_input - second_input - third_input - fourth_input - fifth_input - sixth_input - seventh_input - eighth_input - nineth_input - tenth_input
    print(number_difference)