def message_func(message):
    words=message.split(" ")
    list={
        "sad": "awww",
        "good": "well done"
    }
    output=""
    for char in words:
        output += list.get(char,char) + " "
    return output
message =input("Type a message : ")
res= message_func(message)
print(res)        