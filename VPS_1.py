# input = (()))

data = int(input())

for i in range(data):
    list = []
    data2 = input()

    for j in data2:
        if j == '(':
            list.append(j)
        elif j == ')':
            if list:
                list.pop()
            else :
                print("NO")
                break

    else :
        if not list:
            print("YES")
        else :
            print("NO")