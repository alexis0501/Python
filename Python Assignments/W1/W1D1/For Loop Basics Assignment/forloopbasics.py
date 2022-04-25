for x in range(0,151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("coding")
    else: print(x)

y = 0
for x in range(0,500001):
    if x % 2 == 1:
        y = y + x
print(y)

for x in range(2018, 0, -4):
    print(x)


lowNum = 2
highNum = 30
mult = 2

for x in range(lowNum, highNum, mult):
        if x % mult == 0:
            print(x)

