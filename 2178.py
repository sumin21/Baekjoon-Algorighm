
def miro(arr, a, b):
    visit, noVisit = list(), list()
    node = [0, 0]  # 현재 위치

    arr[0][0] = 1
    noVisit.append(node)
    while len(noVisit):
        node = noVisit.pop(0)

        x = node[0]
        y = node[1]

        count = arr[x][y]

        if(x == (a-1) and y == (b-1)):
            break

        arr2 = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for i in arr2:
            if(i[0] < 0 or i[0] >= a or i[1] < 0 or i[1] >= b):
                continue
            if(arr[i[0]][i[1]] != '1'):
                continue
            new = [i[0], i[1]]
            noVisit.append(new)
            arr[i[0]][i[1]] = count+1

    return arr[a-1][b-1]


arr1 = list(map(int, input().split()))
arr = []

for i in range(arr1[0]):
    str = input()
    arr2 = list(str)
    arr.append(arr2)

result = miro(arr, arr1[0], arr1[1])
print(result)
