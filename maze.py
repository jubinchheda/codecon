#This is throwaway code for a programming contest

import sys
from sys import stdin
import fileinput



def traverse(paramList, visited, current, dimx, dimy):
   #print "visited:",visited
   #print current
   if(current[0] == dimx - 2 and current[1] == dimy - 1):
      visited.append(current)
      return 1
   if(current[0] - 1 >= 0 and paramList[current[0]-1][current[1]] == '_' and [current[0]-1,current[1]] not in visited):
      visited.append(current)
      next = [current[0]-1,current[1]]
      if(traverse(paramList, visited, next, dimx, dimy)):
         return 1
      else:
         del visited[-1]
   if(current[1] - 1>=0 and paramList[current[0]][current[1]-1] == '_'  and [current[0],current[1]-1] not in visited):
      visited.append(current)
      next = [current[0],current[1]-1]
      if(traverse(paramList, visited, next, dimx, dimy)):
         return 1
      else:
         del visited[-1]
   if(current[0] +  1<=dimx -1 and  paramList[current[0]+1][current[1]] == '_'  and [current[0]+1,current[1]] not in visited):
      visited.append(current)
      next = [current[0]+1,current[1]]
      if(traverse(paramList, visited, next, dimx, dimy)):
         return 1
      else:
         del visited[-1]
   if(current[1] + 1<= dimy-1 and paramList[current[0]][current[1]+1] == '_'  and [current[0],current[1]+1] not in visited):
      visited.append(current)
      next = [current[0],current[1]+1]
      if(traverse(paramList, visited, next, dimx, dimy)):
         return 1
      else:
         del visited[-1]
   return 0 # fail


paramList = []
stringList =[]
for line in fileinput.input():
   stringList.append(line.rstrip())

dimStr = stringList[0]
dimList = dimStr.split(" ")
dimx = int(dimList[0])
dimy = int(dimList[1])
#print dimx, dimy
del stringList[0]

for item in stringList:
   paramList.append(list(item))

#print paramList

current = [1,0]
visited =[]
traverse(paramList, visited, current, dimx, dimy)
for i in visited:
   printStr =str(i[0])+","+str(i[1])
   print printStr


