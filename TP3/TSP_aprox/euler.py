def sub(visited, _cur, graph):
    if not graph:
        return visited + [_cur]
    for i, edge in enumerate(graph):
        cur, nex, weight = edge
        if _cur not in edge:
            continue
        _graph = graph[:]
        del _graph[i]
        if _cur == cur:
            res = sub(visited + [cur], nex, _graph)
        else:
            res = sub(visited + [nex], cur, _graph)
        if res:
            return res


def find_eulerian_tour(graph):
    head, tail = graph[0], graph[1:]
    prev, nex, weight = head
    return sub([prev], nex, tail)