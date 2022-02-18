n = int(input())

for i in range(n):
    s = input()
    arr = []
    for k in s:
        arr.append(k)

    score = 0
    beforVal = 0

    for k in arr:
        if (beforVal != 0 and k == 'O'):
            beforVal += 1
        elif (k == 'O'):
            beforVal = 1
        else:
            beforVal = 0

        score += beforVal

    print(score)
