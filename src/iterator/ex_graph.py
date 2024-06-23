"""
Iterator Design Pattern

Example: Graph Traversal
There are many ways to traverse a graph, such as breadth-first search (BFS) 
and depth-first search (DFS). This example demonstrates how to implement the
Iterator Design Pattern to traverse a graph using both BFS and DFS.
"""
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable


class Graph:
    """Graph represents a simple graph using an adjacency list."""

    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_edge(self, v1: int, v2: int) -> None:
        """
        Adds an edge from vertex v1 to vertex v2.

        Args:
            v1 (int): The starting vertex.
            v2 (int): The ending vertex.
        """
        if v1 not in self.adjacency_list:
            self.adjacency_list[v1] = []
        self.adjacency_list[v1].append(v2)

class GraphIterator(Iterator, ABC):
    """GraphIterator defines the interface for iterators over a graph."""

    def __init__(self, graph: Graph, start: int) -> None:
        """
        Initializes the iterator with a graph and a starting vertex.

        Args:
            graph (Graph): The graph to traverse.
            start (int): The starting vertex for the traversal.
        """
        self.graph = graph
        self.start = start
        self._initialize_traversal()

    @abstractmethod
    def _initialize_traversal(self) -> None:
        """Initializes the traversal structure."""
        pass

    @abstractmethod
    def __next__(self) -> int:
        """Returns the next vertex in the traversal."""
        pass

class BFSIterator(GraphIterator):
    """BFSIterator performs a breadth-first traversal of the graph."""

    def _initialize_traversal(self) -> None:
        """Initializes the queue and visited set for BFS."""
        self.queue = [self.start]
        self.visited = set()

    def __next__(self) -> int:
        """
        Returns the next vertex in the BFS traversal.
        """
        while self.queue:
            vertex = self.queue.pop(0)
            if vertex not in self.visited:
                self.visited.add(vertex)
                self.queue.extend(self.graph.adjacency_list.get(vertex, []))
                return vertex
        raise StopIteration

class DFSIterator(GraphIterator):
    """DFSIterator performs a depth-first traversal of the graph."""

    def _initialize_traversal(self) -> None:
        """Initializes the stack and visited set for DFS."""
        self.stack = [self.start]
        self.visited = set()

    def __next__(self) -> int:
        """
        Returns the next vertex in the DFS traversal.
        """
        while self.stack:
            vertex = self.stack.pop()
            if vertex not in self.visited:
                self.visited.add(vertex)
                self.stack.extend(reversed(self.graph.adjacency_list.get(vertex, [])))
                return vertex
        raise StopIteration

class GraphIterable(Iterable):
    """GraphIterable provides iterable interfaces for traversing a graph."""

    def __init__(self, graph: Graph, start: int) -> None:
        """
        Initializes the iterable with a graph and a starting vertex.

        Args:
            graph (Graph): The graph to traverse.
            start (int): The starting vertex for the traversal.
        """
        self.graph = graph
        self.start = start

    def __iter__(self) -> Iterator[int]:
        """
        Returns an iterator for BFS traversal.

        Returns:
            Iterator[int]: An iterator for BFS traversal.
        """
        return BFSIterator(self.graph, self.start)

    def dfs_iterator(self) -> Iterator[int]:
        """
        Returns an iterator for DFS traversal.

        Returns:
            Iterator[int]: An iterator for DFS traversal.
        """
        return DFSIterator(self.graph, self.start)


# Usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

graph_iterable = GraphIterable(graph, 1)

print("BFS Traversal:")
for vertex in graph_iterable:
    print(vertex)

print("\nDFS Traversal:")
for vertex in graph_iterable.dfs_iterator():
    print(vertex)
