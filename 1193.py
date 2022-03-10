x = int(input())

tmp = 1
i = 1
bo = True  # 아

while True:
    if(i <= x):
        i += tmp
        tmp += 1
        bo = not bo
    else:
        tmp -= 1
        i -= tmp
        break

result = 0
if(bo):
    result = [(x-i+1), (tmp-(x-i))]
else:
    result = [tmp-(x-i), (1+(x-i))]

print(str(result[0])+'/'+str(result[1]))
