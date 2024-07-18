user_expression = input("Expression: ")

if user_expression.__contains__("+"):

    user_list = user_expression.split("+")
    print(float(user_list[0]) + float(user_list[1]))

elif user_expression.__contains__("-"):

    user_list = user_expression.split("-")
    print(float(user_list[0]) - float(user_list[1]))

elif user_expression.__contains__("*"):

    user_list = user_expression.split("*")
    print(float(user_list[0]) * float(user_list[1]))

elif user_expression.__contains__("/"):

    user_list = user_expression.split("/")
    if user_list[1] == "0":
        print("You can't divide a number by 0")
    else:
        print(round(float(user_list[0]) / float(user_list[1]), 1))
    