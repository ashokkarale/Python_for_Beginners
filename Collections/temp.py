message="welcome to Mysore"
word=message[-7:]
if(word=="Mysore"):
    print("got it")
else:
    message=message[3:14]
    print(message)