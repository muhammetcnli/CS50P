user_input = input("Expression: ")

sum = ""

userlist = user_input.split()


if len(userlist) == 0:
    print("You don't enter anything.")

elif userlist[1] == "+":

    sum = float(userlist[0]) + float(userlist[2])

elif userlist[1] == "-":

    sum = float(userlist[0]) - float(userlist[2])

elif userlist[1] == "*":

    sum = float(userlist[0]) * float(userlist[2])

elif userlist[1] == "/" and userlist[2] == "0":

    print("You can't divide a number by 0.")

elif userlist[1] == "/":
     
     sum = round(float(userlist[0]) / float(userlist[2]), 1)
else:
    print("Wrong input.")

print(sum)