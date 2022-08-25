from itertools import permutations
arr = input().split(' ')
arr = list(permutations(arr[0], int(arr[1])))
