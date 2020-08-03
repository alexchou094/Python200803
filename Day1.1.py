w = input("Your body weight (kilogram) : ")
h = input("Your height (centimeter) : ")
w = int(w)
h = float(h)
x = w//(h/100)**2
if x<18.5:
    print("Underweight")
elif x<24:
    print("Normal")
elif x<27:
    print("Overweight")
elif x<30:
    print("Mild obesity")
elif x<35:
    print("Moderate obesity")
else:
    print("Severe obesity")