def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) == 0:
        return False
    
    for char in s:
        if len(s) == 1:
            return False
        
        if s[0].isdigit() or s[1].isdigit():
            # checking for starting with 2 letters
            return False
        elif len(s) > 6 or len(s) < 2:
            # checking for length restrictions
            return False
        elif not char.isdigit() and not char.isalpha():
            # checking for punctuations etc.
            return False
        elif char.isdigit():
            numlist = s[s.index(char):]
            print(numlist)
            for num in numlist:
                if not num.isdigit():
                    return False
            
            if numlist[0] == "0":
                return False
            


            return True
                
        
    return True

    
main()