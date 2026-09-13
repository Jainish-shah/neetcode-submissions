from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # Build the directed graph.
        graph = defaultdict(list)
        for source, destination, travel_time in times:
            graph[source].append((destination, travel_time))

        # Store the shortest known time to each node.
        distances = [float("inf")] * (n + 1)
        distances[k] = 0

        # Process nodes in increasing order of current travel time.
        min_heap = [(0, k)]

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            # Ignore an outdated heap entry.
            if current_time > distances[node]:
                continue

            # Relax all outgoing edges.
            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        # If any node is unreachable, the signal cannot reach everyone.
        maximum_time = max(distances[1:])

        return -1 if maximum_time == float("inf") else maximum_time