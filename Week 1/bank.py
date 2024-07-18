key_word = "hello"

user_greeting = input("Greeting: ")

# checking if user input contains any sorts of hello
if user_greeting.lower().split(sep=" ").__contains__(key_word) or user_greeting.lower().split(sep=",").__contains__(key_word):
    print(f"$0")
elif len(user_greeting) == 0:
    print("$100")
elif user_greeting[0].lower() == "h":
    print("$20")
else:
    print("$100")