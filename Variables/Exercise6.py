age = int(user)
i = int(1)
b = int(10)
if i < 2 :
    print("In " + str(b) + "years, you will be" + str(age + b)
          + "years old.")
    i = i + 1
    b = b + 10
elif i < 5 :
    print("\nIn " + b + "years, you will be" + (age + b) +
          "years old.")
    i = i + 1
    b = b + 10