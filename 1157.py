s = input()

arr = list(s.upper())
arr2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr3 = [0 for k in range(26)]

for i in range(len(arr2)):
    arr3[i] = arr.count(arr2[i])

m = max(arr3)

if(arr3.count(m) > 1):
    print('?')
else:
    print(arr2[arr3.index(m)])
