def virus(obj):
    nonVisit, visit = list(), list()
    node = 1

    nonVisit.append(node)

    while len(nonVisit):
        node = nonVisit.pop()
        arr = []
        if not node in visit:
            if(node != 1):
                visit.append(node)
            nonVisit.extend(obj[node])

    return visit


# 확정 아니면 visit으로 내보내지 않기


n = int(input())
nn = int(input())

obj = {}

for i in range(nn):
    arr1 = list(map(int, input().split()))
    if not arr1[0] in obj:
        obj[arr1[0]] = []
    obj[arr1[0]].append(arr1[1])
    if not arr1[1] in obj:
        obj[arr1[1]] = []
    obj[arr1[1]].append(arr1[0])

result = virus(obj)
result.sort()

print(len(result))
