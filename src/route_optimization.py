"""Dijkstra's algorithm implementation for route optimization"""

import heapq
from typing import Dict, Any


def dijkstra(graph_data: Dict[str, Dict[str, int]], start: str) -> Dict[str, float]:
    """Calculate shortest paths in a weighted graph using Dijkstra's algorithm

    Args:
        graph_data: Graph structure as {node: {neighbor: weight}}
        start: Starting node for path calculation

    Returns:
        Dictionary of shortest distances to all nodes
    """
    distances = {node: float("inf") for node in graph_data}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph_data[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    # Example graph (nodes and traffic-weighted edges)
    sample_graph = {
        "A": {"B": 5, "C": 2},
        "B": {"A": 5, "D": 4},
        "C": {"A": 2, "D": 7},
        "D": {"B": 4, "C": 7},
    }

    optimal_routes = dijkstra(sample_graph, "A")
    print(f"Optimal Routes from A: {optimal_routes}")
