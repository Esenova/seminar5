from myalgorithm import MyAlgorithm


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
    
