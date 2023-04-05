def divisor(num):
    listdivisor = []
    for i in range(2,num):
        if num % i == 0:
            listdivisor.append(i)
    return listdivisor
while True:
    num = int(input("Number: "))
    if(num == "q" or num == "Q"):
        print("Program has stopped.")
        break
    else:
        print("Divisors: ",divisor(num))

