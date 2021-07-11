#!/usr/bin/env python3
from heapq import nsmallest
from itertools import filterfalse

def second_smallest(numbers):
	s=set()
	sa=s.add
	un=(sa(n) or n for n in filterfalse(s.__contains__,numbers))
	return nsmallest(2,un)[-1]
mylist=[]
scorelist=[]
for i in range(int(input())):
        name = input()
        score = float(input())
        ele=[name,score]
        mylist.append(ele)
        scorelist.append(score)
ssmallest=second_smallest(scorelist)
names=[]
for i in range(len(mylist)):
	if mylist[i][1] == ssmallest:
		names.append(mylist[i][0])
print(sorted(names))
