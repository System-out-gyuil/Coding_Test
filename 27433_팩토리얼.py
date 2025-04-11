n = int(input())

num = 1
result = 1

for i in range(n-1):
    result += num * result
    num += 1

print(result)