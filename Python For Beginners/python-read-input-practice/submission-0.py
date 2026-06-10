def add_two_numbers() -> int:
    user_input = input()
    num_list = user_input.split(",")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list[0] + num_list[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
