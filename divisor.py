number = int(input("Gimme the number: "))
numberList = range(1, number)
resp = []
resp.append(number)
for x in numberList:
    if number%x == 0:
        resp.append(x)

resp.sort()
print (resp)