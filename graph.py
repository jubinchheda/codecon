import sys
from sys import stdin
import fileinput

def find_all_paths(graph, start, end, path):
   path = path + [start]
   if start == end:
      return [path]
   if not graph.has_key(start):
      return []
   paths = []
   for node in graph[start]:
      if node not in path:
         newpaths = find_all_paths(graph, node, end, path)
         for newpath in newpaths:
            paths.append(newpath)
   return paths               
            
graph = {}

paramList = []
stringList =[]
for line in fileinput.input():
   stringList.append(line.rstrip())

for item in stringList:
   paramList.append(list(item.split()))

#print paramList

N = int(stringList[0])


del paramList[0]
for elem in paramList:
   if elem[0] in graph.keys():
      current = graph[elem[0]]
      current.append(elem[1])
      graph[elem[0]]=current
   else:
      graph[elem[0]] = [elem[1]]

#print graph

   

#print paramList
print len(find_all_paths(graph, 'JFK', 'SFO',[]))

#[digit, size, [i,j], [iopp. jopp]]
