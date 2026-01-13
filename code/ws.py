import matplotlib.pyplot as plt
import numpy as np
from graphs import generateWattsStrogatz
from models import MTAEGraphs, MTPEGraphs

if __name__ == "__main__":
  lamb = 1
  alpha = 1
  tend = 100000
  population = 1000
  ini = 100

  repTotGraph = 5
  repTot = 100

  rang = np.linspace(0.0, 1.0, 25)

  data = {}

  for ind, k in enumerate([5, 10, 50, 100]):

    propMTAE = []
    propMTPE = []

    for p in rang:

      mtae = 0
      mtpe = 0

      for repg in range(repTotGraph):

        graph = generateWattsStrogatz(population, k, 0.5)

        for rep in range(repTot):

          t, I, S, R = MTAEGraphs(graph, lamb, alpha, p, tend, ini)
          t1, I1, S1, R1 = MTPEGraphs(graph, lamb, alpha, p, tend, ini)

          mtae += I[-1]
          mtpe += I1[-1]

      mtae /= repTot * repTotGraph
      mtpe /= repTot * repTotGraph

      propMTAE.append(mtae / population)
      propMTPE.append(mtpe / population)

    print(k)
    data[k] = {}
    data[k]["MTAE"] = propMTAE
    data[k]["MTPE"] = propMTPE

  colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

  for k in data:
    print(k)
    plt.plot(rang, data[k]["MTAE"], label="MTAE", color=colors[0], linestyle='-')
    plt.plot(rang, data[k]["MTPE"], label="MTPE", color=colors[1], linestyle='-')
    plt.xlabel("$p$")
    plt.ylabel(r"$x_{\infty}$")
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.legend()
    plt.show()
