x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
delta = y ** 2 - 4 * x * z
r1 = (-y - (delta ** 0.5)) / (2 * x)
r2 = (-y + (delta ** 0.5)) / (2 * x)
print("First root is: {}\n"
      "Second root is: {}\n".format(r1,r2))
