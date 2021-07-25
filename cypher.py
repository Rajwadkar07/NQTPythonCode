def ecrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isspace()):
            result += " "
        elif (char.isdigit()):
            result += str(int(char)+key)
        else:
            result += (chr(ord(char)+key))
    return result
    
text = input("Enter msg: ")
key = int(input("Enter key: "))
print(ecrypt(text,key))