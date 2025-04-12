from itertools import *

list1 = []

for i in range(9):
  list1.append(int(input()))

#  모든 경우의 수 가져오기(배열, 가져올 요소 개수)
lists = list(permutations(list1, 7))

for i in lists:
  num = 0

  for j in i:
    num += j

  if num == 100:
    for k in sorted(i):
      print(k)
    break