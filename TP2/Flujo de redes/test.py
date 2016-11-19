from MaxFlow import FlowNetwork

INF = 99999

# Areas
areas = ["Marketing", "Telecomunicaciones", "Inteligencia Artificial", "Desarrollo", "Infraestructura", "Calidad"]
costs = [2, 5, 10, 4, 6, 4]

print "AREAS DE REQUERIMIENTOS EXISTENTES"
for i in xrange(len(areas)):
    print "Area:", areas[i], "\tCosto:", costs[i]

print

# Proyectos
PROJECTS_COUNT = 4
projects = {'o': "Proyecto1", 'p': "Proyecto2", 'q': "Proyecto3", 'r': "Proyecto4"}
revenues = [1, 20, 50, 40]

print "PROYECTOS DISPONIBLES"
for i in xrange(len(projects)):
    items = projects.items()
    print "Proyecto:", items[i][0] + ":", items[i][1], "\tGanancia:", revenues[i]

print

# Grafo
#   vertices:
#       - s: origen
#       - t: destino

#       - o: proyecto 1
#       - p: proyecto 2
#       - q: proyecto 3
#       - r: proyecto 4

#       - u: requerimiento 1
#       - v: requerimiento 2
#       - w: requerimiento 3
#       - x: requerimiento 4
#       - y: requerimiento 5
#       - z: requerimiento 5

g = FlowNetwork()
[g.add_vertex(v) for v in "sopqruvwxyzt"]



# aristas


g.add_edge('s','o', revenues[0])
g.add_edge('s','p', revenues[1])
g.add_edge('s','q', revenues[2])
g.add_edge('s','r', revenues[3])

# proyecto 1
g.add_edge('o','u', INF)
g.add_edge('o','v', INF)

# proyecto 2
g.add_edge('p','w', INF)

# proyecto 3
g.add_edge('q','w', INF)
g.add_edge('q','x', INF)
g.add_edge('q','y', INF)
g.add_edge('q','z', INF)

# proyecto 4
g.add_edge('r','u', INF)
g.add_edge('r','v', INF)
g.add_edge('r','x', INF)


g.add_edge('u','t', costs[0])
g.add_edge('v','t', costs[1])
g.add_edge('w','t', costs[2])
g.add_edge('x','t', costs[3])
g.add_edge('y','t', costs[4])
g.add_edge('z','t', costs[5])


print "MAX_FLOW", (g.max_flow('s','t'))
print "MIN_CUT", g.find_min_cut('s', [])
print "POYECTOS REALIZADOS"
for result in g.find_min_cut('s', []):
    if result.sink in projects:
        print "\t", result.sink + ":", projects[result.sink]
