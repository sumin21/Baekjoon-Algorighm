def dfs(ob, start):
    for key, value in ob.items():
        value.sort(reverse=True)

    noVisit, visit = list(), list()
    noVisit.append(start)

    while len(noVisit):
        node = noVisit.pop()
        if node not in visit:
            visit.append(node)
            noVisit.extend(ob[node])

    return visit


def bfs(ob, start):
    for key, value in ob.items():
        value.sort()

    noVisit, visit = list(), list()
    noVisit.append(start)

    while len(noVisit):
        node = noVisit.pop(0)
        if node not in visit:
            visit.append(node)
            noVisit.extend(ob[node])
    return visit


arr1 = list(map(int, input().split()))
obj = {}
for i in range(1, arr1[0]+1):
    obj[i] = []

for i in range(arr1[1]):
    arr2 = list(map(int, input().split()))
    obj[arr2[0]].append(arr2[1])
    obj[arr2[1]].append(arr2[0])

result1 = dfs(obj, arr1[2])
result2 = bfs(obj, arr1[2])

for i in result1:
    print(i, end=' ')

print()
for i in result2:
    print(i, end=' ')
