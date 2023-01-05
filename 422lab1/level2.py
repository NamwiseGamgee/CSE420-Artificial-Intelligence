def bfs(stNode, desNode, graph, nodes, edges):
    mainQ = []
    vL = [False for i in range(nodes)]
    cost = [0 for i in range(nodes)]

    mainQ.append(stNode)

    while mainQ:
        stNode = mainQ[0]
        if stNode == desNode:
            return cost[stNode]
        else:
            vL[mainQ.pop(0)] = True

            for i in range(len(graph[stNode])):
                if vL[graph[stNode][i]] != True:
                    mainQ.append(graph[stNode][i])
                    vL[graph[stNode][i]] = True
                    cost[graph[stNode][i]] = cost[stNode] + 1


if __name__ == '__main__':
    f = open("bfs2.txt")
    nodes = int(f.readline())
    edges = int(f.readline())
    graph = [[] for i in range(nodes)]

    for i in range(edges):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    destination = int(f.readline())
    noraPos=int(f.readline())
    laraPos=int(f.readline())

    noraSteps=bfs(noraPos, destination, graph, nodes, edges)
    laraSteps=bfs(laraPos, destination, graph, nodes, edges)

    if laraSteps > noraSteps:
        print("Nora Wins")
    elif laraPos == noraPos :
        print("It is a tie")
    else:
        print("Lara Wins")