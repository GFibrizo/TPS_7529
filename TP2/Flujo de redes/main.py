from MaxFlow import FlowNetwork

INF = 99999

area_count = int(raw_input())
project_count = int(raw_input())

areas = {}
for i in xrange(1, area_count+1):
    cost = int(raw_input())
    areas["req_" + str(i)] = cost

projects_revenues = {}
projects_reqs = {}

for i in xrange(1, project_count+1):
    project_str = raw_input()
    project = project_str.split()
    proj_id = "proy_" + str(i)
    projects_revenues[proj_id] = int(project[0])
    projects_reqs[proj_id] = map(lambda x: "req_" + str(x), project[1:])



g = FlowNetwork()
g.add_vertex('s')
g.add_vertex('t')
[g.add_vertex(v) for v in projects_revenues.keys()]
[g.add_vertex(v) for v in areas.keys()]


for proj in projects_revenues.keys():
    print "arista", "s -> " + proj
    g.add_edge('s', proj, projects_revenues[proj])

for proj in projects_reqs.keys():
    reqs = projects_reqs[proj]
    for area in reqs:
        print "arista", proj + " -> " + area
        g.add_edge(proj, area, INF)

for area in areas.keys():
    print "arista", area + " -> t"
    g.add_edge(area,'t', areas[area])


print "MAX_FLOW", (g.max_flow('s','t'))
print "MIN_CUT", g.find_min_cut('s', [])
print "POYECTOS REALIZADOS"
for result in g.find_min_cut('s', []):
    if result.sink in projects_revenues:
        print "\t", result.sink + ":", projects_revenues[result.sink]
