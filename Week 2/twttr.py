user_input = input("Input: ")
vowel_list = ["a", "e", "i", "o", "u"]
output = ""
for n in user_input:
    if n.lower() in vowel_list:
        pass
    else:
        output += n

print(f"Output: {output}")