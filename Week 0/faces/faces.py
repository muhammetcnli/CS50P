def covert(contex):
    input_list = contex.split()
    for i in range(len(input_list)):
        if input_list[i] == ":)":
            input_list[i] = "🙂"
        if input_list[i] == ":(":
            input_list[i] = "🙁"
    joined = " ".join(input_list)
    print(joined)

covert(input("Give input: "))
