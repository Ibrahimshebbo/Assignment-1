# movie ticket price calculator 
try:
    age=int(input("Enter your age: "))
    if age < 18:
        print("The ticket price is $5")
    elif age < 30:
        print("The ticket price is $8")
    elif age < 50:
        print("The ticket price is $11")
    else:
        print("The ticket price is $14")
except:
    print("Invalid entry")


