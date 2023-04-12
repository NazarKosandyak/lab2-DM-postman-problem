import heapq


def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    heap = [(0, start)]

    while heap:
        (cost, u) = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v in range(n):
            if graph[u][v] and not visited[v]:
                new_cost = dist[u] + graph[u][v]
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

    return dist


with open('input.txt') as file:
    n = int(file.readline())
    graph = [list(map(int, file.readline().split())) for _ in range(n)]

for i in range(n):
    distances = dijkstra(graph, i)
    print(f'Найкоротша відстань від вершини {i}: {distances}')
