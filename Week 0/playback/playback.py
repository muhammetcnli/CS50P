user_input = input("Give your input: ")

stripped_list = user_input.split()
seperator = "..."
joined_list = seperator.join(stripped_list)
print(joined_list)
