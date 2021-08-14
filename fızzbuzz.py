def fızzbuzz(x):
    for i in range(1,x+1):
        if i % 3 ==0 and i % 5 == 0:
            print("fızzbuzz")
        elif i % 3 == 0:
            print("fızz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
fızzbuzz(100)