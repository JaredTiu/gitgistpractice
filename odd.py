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

for number in number_list: 
    if number % 2 != 0: 
        print("The odd numbers are: ", number)