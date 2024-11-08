first_input = int(input("Input first number: "))
second_input = int(input("Input second number: "))

if first_input > second_input:
    for num in range(second_input + 1, first_input):
        print(num)
else:
    print("invalid")