import heapq
INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
def dijkstra(start):
    q = []
    # (비용, 다음 노드 추가)
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
dijkstra(start)

cnt = 0
max_distance = 0
# 거리가 무한이 아닌게 도달가능한 개수 .
# 도달 가능한 것 중 가장 큰 거리가 최대 걸리는 시간
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)
print(cnt-1, max_distance)