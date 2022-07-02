import json
import random as r
import math
import heapq as hq
import numpy as np
import random
from perlin_noise import PerlinNoise

def bfs(G, s):
  n= len(G)
  visited= [False]*n
  path= [-1]*n # parent
  queue= [s]
  visited[s]= True

  while queue:
    u= queue.pop(0)
    for v, _ in G[u]:
      if not visited[v]:
        visited[v]= True
        path[v]= u
        queue.append(v)

  return path

def dfs(G, s, t):
  n= len(G)
  path= [-1]*n
  visited= [False]*n

  stack= [s]
  while stack:
    u= stack.pop()
    visited[u]= True
    if u == t:
        break
    for v, _ in G[u]:
      if not visited[v]:
        path[v]= u
        stack.append(v)

  return path

def dijkstra(G, s):
    n= len(G)
    visited= [False]*n
    path= [-1]*n
    cost= [math.inf]*n

    cost[s]= 0
    pqueue= [(0, s)]
    while pqueue:
        g, u= hq.heappop(pqueue)
        if not visited[u]:
            visited[u]= True
            for v, w in G[u]:
                if not visited[v]:
                    f= g + w
                    if f < cost[v]:
                        cost[v]= f
                        path[v]= u
                        hq.heappush(pqueue, (f, v))

    return path, cost

def loadCustomG():
    with open("TP_Intersecciones_Final.txt") as f:
        edges = []
        n = 0
        for line in f:
            u, v = [int(x) for x in line.split()]
            edges.append((u-1, v-1, r.randint(1,10)))
            if u > n:
                n = u
            if v > n:
                n = v

        G=[[] for _ in range(n)]
        for u, v, w in edges:
            G[u].append((v,w))
        return G

def loadCustomCoordenates():
    with open('TP_CoordenadasP1.txt') as f:
        lines = f.readlines()

        count = 0
        LOC = []
        for line in lines:
            count += 1
            x = line.split('(')[1]
            x = x.split(')')[0]

            geo = x.split(',')
            geoX = float(geo[0])
            geoY = float(geo[1])
            print(str(geoX) + "," + str(geoY) + " - " + str(count))
            LOC.append((geoX,geoY))
        return LOC

def loadCustomPesos():
    with open("TP_Intersecciones_Final.txt") as f:
        edges = []
        n = 0
        for line in f:
            print(line)

gg = loadCustomG()
Loc2 = loadCustomCoordenates()

def graph():
    return json.dumps({"loc": Loc2 , "g": gg})

def paths(s, t):
    bestpath, _= dijkstra(gg, s)
    path1= bfs(gg, s)
    path2= dfs(gg, s, t)
    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})
