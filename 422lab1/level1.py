def bfs(stNode,desNode,graph,nodes,edges):
    mainQ=[]
    vL=[False for i in range(nodes)]
    cost=[0 for i in range(nodes)]

    mainQ.append(stNode)


    while mainQ:
        stNode=mainQ[0]
        if stNode == desNode:
            print("Minimum steps lagche ", cost[stNode], " ta")
            mainQ.pop(0)
        else:
            vL[mainQ.pop(0)] = True

            for i in range(len(graph[stNode])):
                if vL[graph[stNode][i]]!=True:
                    mainQ.append(graph[stNode][i])
                    vL[graph[stNode][i]]=True
                    cost[graph[stNode][i]]=cost[stNode]+1




if __name__ == '__main__':
    f = open("bfs.txt")
    nodes = int(f.readline())
    edges = int(f.readline())
    graph = [[] for i in range(nodes)]

    for i in range(edges):
        u, v = map(int, f.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    destination = int(f.readline())

    bfs(0,destination,graph,nodes,edges)