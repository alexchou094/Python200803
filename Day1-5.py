s = input("Please enter your score : ")
s = float(s)
if s>=0 and s<=100:
    print("Your score ranking is :")
    if s>=90:
        print("A")
    elif s>=80:
        print("B")
    elif s>=70:
        print("C")
    elif s>=60:
        print("D")
    else:
        print("fail")
else:
    print("The value of score must between 0 and 100 !!")