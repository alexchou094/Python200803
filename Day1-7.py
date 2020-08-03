m = input("What's your math score : ")
e = input("What's your english score : ")
m = float(m)
e = float(e)
if m>=90 and e>=90:
    print("You will be treat")
elif m<60 and e<60:
    print("You will be punish")
elif m<60 or e<60:
    print("Do more exerise")