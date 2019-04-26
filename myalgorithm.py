

class MyAlgorithm:
    def adjacency_matrix(self, vertice, graph):
        matrix = []

        for i in range(0, vertice):
            matrix.append([])
            for j in range(0, vertice):
                matrix[i].append(0)

        for i in range(0, len(graph)):
            matrix[graph[i][0]][graph[i][1]] = graph[i][2]
            matrix[graph[i][1]][graph[i][0]] = graph[i][2]

        return matrix

    def prims(self, vertice, graph):
        matrix = self.adjacency_matrix(vertice, graph)

        vertex = 0
        visited = []
        edges = []
        MST = []
        minEdge = [None, None, float('inf')]

        while len(MST) != vertice - 1:

            visited.append(vertex)

            for r in range(0, vertice):
                if matrix[vertex][r] != 0:
                    edges.append([vertex, r, matrix[vertex][r]])

            for e in range(0, len(edges)):
                if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                    minEdge = edges[e]

            edges.remove(minEdge)

            MST.append(minEdge)

            vertex = minEdge[1]
            minEdge = [None, None, float('inf')]

        return MST


if __name__ == '__main__':
    a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

    graph = [
        [a, b, 2],
        [a, c, 3],
        [b, d, 3],
        [b, c, 5],
        [b, e, 4],
        [c, e, 4],
        [d, e, 2],
        [d, f, 3],
        [e, f, 5]
    ]

    algorithm = MyAlgorithm()
    print(algorithm.prims(6, graph))
