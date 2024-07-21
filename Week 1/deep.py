user_answer = input("What is the answer to Great Question of Life, the Universe and Everything? ").strip()

if user_answer.__contains__("-"):
    user_list = user_answer.split("-")
else:
    user_list = user_answer.split()

user_answer_splitted = " ".join(user_list).lower()

if user_answer == "42":
    print("Yes")
elif user_answer_splitted == "forty two":
    print("Yes")
else:
    print("No")
