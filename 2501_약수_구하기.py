n, k = map(int, input().split())

list = []

for i in range(n):
    if n%(i+1) == 0:
        list.append(i+1)

if len(list) < k:
    print(0)
else : 
    print(list[k-1])