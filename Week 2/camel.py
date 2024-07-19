def main():
    user_input = input("camelCase: ")
    last_input = camel_to_snake(user_input)
    print("snake_case: " + last_input)



def camel_to_snake(user_input):
    result = ""
    for n in user_input:
        if n.isupper():
           # result = user_input.replace(n, "_" + n.lower()) the other way
            result += "_" + n.lower()
        else:
            result += n
    return result

main()












#print(last_word , end=" ")