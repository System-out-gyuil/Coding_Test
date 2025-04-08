# num = list(map(int, input().split()))

# for i in sorted(set(num)):
#     print(i)

# input = 5
#         5
#         2
#         3
#         4
#         1

num = int(input())
list = []

for i in range(num):
    list.append(int(input()))

for i in sorted(list):
    print(i)