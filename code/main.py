import matplotlib.pyplot as plt
import models as mod
import graphs as gr
import numpy as np

def recordLine(data, filename):
  txt = ""
  for d in data:
    txt += str(d) + " "
  txt += "\n"
  with open(filename, "a") as myfile:
    myfile.write(txt)

def type1(population, ini, repTotGraph, repTot, graphGenerator, modelFunction, filename, initAt = 0):
  lamb = 1
  alpha = 1
  tend = 100000

  rang = np.linspace(0.0, 1.0, 41)
  # print(rang)

  for iii in range(initAt, len(rang)):
    pr = rang[len(rang) - iii - 1]
    curr = [0]*len(rang)

    for repGraph in range(repTotGraph):
      graph = graphGenerator(population, pr)

      for i in range(len(rang)):
        p = rang[i]

        for rep in range(repTot):
          t, I, S, R = modelFunction(graph, lamb, alpha, p, tend, ini)
          curr[i] += I[-1]

    for i in range(len(rang)):
      curr[i] /= repTot * repTotGraph
      curr[i] /= population

    recordLine(curr, filename)
    print(iii)

def type2(population, ini, repTotGraph, repTot, graphGenerator, modelFunction, filename, initAt = 0):
  lamb = 1
  alpha = 1
  tend = 100000

  rang = np.linspace(0.0, 1.0, 41)
  rang2 = np.linspace(2, 82, 41)
  # print(rang)

  for iii in range(initAt, len(rang2)):
    pr = rang2[len(rang2) - iii - 1]
    curr = [0]*len(rang)

    for repGraph in range(repTotGraph):
      graph = graphGenerator(population, int(pr))

      for i in range(len(rang)):
        p = rang[i]

        for rep in range(repTot):
          t, I, S, R = modelFunction(graph, lamb, alpha, p, tend, ini)
          curr[i] += I[-1]

    for i in range(len(rang)):
      curr[i] /= repTot * repTotGraph
      curr[i] /= population

    recordLine(curr, filename)
    print(iii)

if __name__ == "__main__":
  type1(1000, 100, 5, 100, gr.generateErdosRenyi, mod.MTAEGraphs, "mtae.txt")
  type1(1000, 100, 5, 100, gr.generateErdosRenyi, mod.MTPEGraphs, "mtpe.txt")
  type2(1000, 100, 5, 100, gr.generateBarabasiAlbert, mod.MTAEGraphs, "mtae2.txt")
  type2(1000, 100, 5, 100, gr.generateBarabasiAlbert, mod.MTPEGraphs, "mtpe2.txt")
  type1(1000, 100, 5, 100, lambda pop, pr : gr.generateWattsStrogatz(pop, 5, pr), mod.MTAEGraphs, "mtae3.txt")
  type1(1000, 100, 5, 100, lambda pop, pr : gr.generateWattsStrogatz(pop, 5, pr), mod.MTPEGraphs, "mtpe3.txt")