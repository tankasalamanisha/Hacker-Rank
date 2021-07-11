#!/usr/bin/env python3

n = int(input())
arr = list(map(int, input().split()))
sortarr= list(sorted(set(arr)))
print(sortarr[-2])
