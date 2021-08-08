def prime_factors(n):
    lst = []
    for i in range(2,n):
        if n % i == 0:
            while n % i == 0:
                lst.append(i)
                n = n / i
    return lst 
