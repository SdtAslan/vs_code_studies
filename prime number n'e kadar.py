y = input("Enter a positive number")
if y.isdigit():
    x = int(y)
    liste = []
    for k in range(2,x +1):
        count = 0
        for i in range(1, k + 1):
            if (k % i) == 0:
                count += 1
        if count <= 2:
            liste.append(k)      
    print("prime numbers up to:",x, ">>", liste)
    
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")