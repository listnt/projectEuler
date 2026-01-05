import heapq
import sys

triangle="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = triangle.split('\n')
triangle = [list(map(int, line.split(' '))) for line in triangle]
total = sum([len(row) for row in triangle])

graph={}
i=0
for row in triangle:
    for col in row:
        graph[i]={"val": col}
        if i + len(row) < total:
            graph[i]["left"] = i+len(row)
        if i + len(row) + 1 < total:
            graph[i]["right"] = i + len(row) + 1
        i+=1

adj = []
for i in range(total):
    adj.append([])
    if graph[i].get("left"):
        adj[i].append((graph[i]["left"],graph[graph[i]["left"]]["val"]))
    if graph[i].get("right"):
        adj[i].append((graph[i]["right"],graph[graph[i]["right"]]["val"]))

def dijkstra(adj,src):
    V = len(adj)
    pq = []
    dist = [0] * V
    dist[src] = 75
    heapq.heappush(pq, (75, src))
    while pq:
        d, u = heapq.heappop(pq)
        if d < dist[u]:
            continue

        for v, w in adj[u]:
            if v >= len(dist):
                continue
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
paths = dijkstra(adj,0)
print(max(paths))