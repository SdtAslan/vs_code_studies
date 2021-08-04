y = input("Enter a positive number")
if y.isdigit():
    x = int(y)
    liste = [2]
    k = 3
    while k < x + 1:
        count = 0
        for i in range(2, k):
            if (k % i) == 0:
                count += 1
        if count < 1:
            liste.append(k)
        k +=1        
    print(liste)
    
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")