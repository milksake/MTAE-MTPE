import networkx as nx

def generateRing(N, r = 2):
  r = r // 2
  graph = []
  for i in range(0, N):
    neigh = []
    for j in range(1, r+1):
      neigh.append((i + j) % N)
      neigh.append(((i - j) + N) % N)
    graph.append(neigh)
  return graph

def generateComplete(N):
  graph = []
  for i in range(0, N):
    neigh = []
    for j in range(0, N):
      if i != j:
        neigh.append(j)
    graph.append(neigh)
  return graph

def generateErdosRenyi(N, p):
  graph = []
  g = nx.fast_gnp_random_graph(N, p)
  for n, nbrs in g.adj.items():
    neigh = []
    for nbr, eattr in nbrs.items():
      neigh.append(nbr)
    graph.append(neigh)
  return graph

def generateBarabasiAlbert(N, m):
  graph = []
  g = nx.barabasi_albert_graph(N, m)
  for n, nbrs in g.adj.items():
    neigh = []
    for nbr, eattr in nbrs.items():
      neigh.append(nbr)
    graph.append(neigh)
  return graph

def generateWattsStrogatz(N, k, p):
  graph = []
  g = nx.watts_strogatz_graph(N, k, p)
  for n, nbrs in g.adj.items():
    neigh = []
    for nbr, eattr in nbrs.items():
      neigh.append(nbr)
    graph.append(neigh)
  return graph