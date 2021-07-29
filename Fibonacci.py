fibonacci = []
x = 0
y = 1
while y <= 55:                     
    x, y = y, x+y

    fibonacci.append(x)
print(fibonacci)