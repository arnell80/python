#logical operators (and,or, not) = used to check if two or more conditions statemnents

temp = int(input("what is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is nice today!:")
    print("Go outside today!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!:")
    print("Stay inside today!")


if not (temp >= 0 and temp <= 30):
    print("the temperature is bad today!:")
    print("Stay inside today!")
elif not() temp < 0 or temp > 30):
    print("the temperature is nice today!:")
    print("Go outside today!")

