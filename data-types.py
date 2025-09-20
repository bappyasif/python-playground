temp = 99
print(temp, type(temp))
temp = float(temp)
print(temp, type(temp))

temp = 99.99
print(temp, type(temp))
temp = int(temp)
print(temp, type(temp))

temp = 99.99
print(temp, type(temp))
temp = float(temp)
print(temp, type(temp))

raining = True
print(raining, type(raining))
raining = bool("True")
print(raining, type(raining))

raining = False
print(raining, type(raining))
raining = str("False")
print(raining, type(raining))


def types():
    temp = int(99.99)
    print(temp, type(temp))

    temp = float(101.2)
    print(temp, type(temp))

    temp = bool(101.2)
    print(temp, type(temp))

    temp = str(101.2)
    print(temp, type(temp))

types()