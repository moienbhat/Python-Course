import heapq

def dijkstra(n, edges, src):
    graph = {i: [] for i in range(n)}

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))   # remove if directed graph

    dist = [float('inf')] * n
    dist[src] = 0

    pq = [(0, src)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for nei, w in graph[node]:
            if dist[node] + w < dist[nei]:
                dist[nei] = dist[node] + w
                heapq.heappush(pq, (dist[nei], nei))

    return dist



if __name__ == "__main__":
    n = 5
    edges = [
        (0, 1, 2),
        (0, 2, 5),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 3),
        (3, 4, 1)
    ]
    src = 0

    result = dijkstra(n, edges, src)
    print("Shortest distances from source 0:")
    print(result)
