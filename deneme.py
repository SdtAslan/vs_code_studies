y = input("Enter a number > learn to is it prime number")
if y.isdigit():
    x = int(y)
    if x < 2:
        a = "is not a prime number"
    elif x >= 2:
        for i in range(2, x):
            if x % i == 0:
                a = "is not a prime number"
    else:
        a = "is a prime number"         
    print(x, a)
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")