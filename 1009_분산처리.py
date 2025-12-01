T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    x = str(a ** b)

    x = x[-1::]

    print(x)
