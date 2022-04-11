##      0  1   2
##  0   0   7   5
##  1   7   0  무한
##  2   5  무헌  0
INF = 999999999
graph1 = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0],
]#인접행렬
graph  = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)
#인접list

# 메모리측면은 인접list가 효율적 하지만 탐색은 느리다 

# def dfs(graph,v,visitd):
#     visitd[v] = True
#     print(v,end = '')
#     for i in graph[v]:
#         if not visitd[i]:

