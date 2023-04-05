num1 = 1
num2 = 1
fibonacci = [num1, num2]
for i in range(20):
    num1, num2 = num2, num1+num2
    fibonacci.append(num2)
print(fibonacci)
