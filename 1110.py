n = int(input())

cycle = 0
newNum = n

while(cycle == 0 or n != newNum):
    a = newNum % 10
    c = (newNum//10) + a
    d = c%10

    newNum = a*10 + d
    cycle += 1

print(cycle)
