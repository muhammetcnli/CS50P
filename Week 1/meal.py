def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    if time == "":
        pass
    else:
        hours, mins = time.split(":")

        new_time = float(f"{hours}.{mins}")

        if 18.0 <= new_time <= 19.0:
            print("dinner time")

        elif 12.0 <= new_time <= 13.0:
            print("lunch time")

        elif 7.0 <= new_time <= 8.0:
            print("breakfast time")
        
        else:
            pass

if __name__ == "__main__":
    main()