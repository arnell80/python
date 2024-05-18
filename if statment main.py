#if statmemnt = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

if age > 120:
    print("Yeah Right!  You must can't count!  JAJAJAJAJA!!")

elif age >= 100:
    age1 = str(age)
    slice = slice(1, 3)
    age2 = age1[slice]
    print("You've cleared a century by", age2, "years!")

elif age < 0:
    print("You havent been born yet!")
elif age >= 18:
    print("You are an adult!")
else:
    print("You are a child!")