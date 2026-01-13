import matplotlib.pyplot as plt
import numpy as np

def generateHeatMap(filename, title, type):
  data = []
  with open(filename) as file:
    for line in file:
      data.append([float(x) for x in line.split()])

  left = -0.0125
  right = 1.0125
  bottom = -0.0125
  top = 1.0125
  extent = [left, right, bottom, top]

  plt.imshow( data, extent=extent, vmin=0.0, vmax=1.0 )
  if type == 2:
    plt.yticks(np.linspace(0.0, 1.0, 6), np.linspace(2, 82, 6))

  plt.colorbar(label=r"$x_{\infty}$")
  if (title):
    plt.title( title )
  plt.xlabel("$p$")
  plt.ylabel("$q$")
  plt.show()

def generateHeatMapDiff(filename1, filename2, title, type):
  data1 = []
  with open(filename1) as file:
    for line in file:
      data1.append([float(x) for x in line.split()])
  data2 = []
  with open(filename2) as file:
    for line in file:
      data2.append([float(x) for x in line.split()])

  for i in range(len(data1)):
    for j in range(len(data1[0])):
      data1[i][j] -= data2[i][j]

  left = -0.0125
  right = 1.0125
  bottom = -0.0125
  top = 1.0125
  extent = [left, right, bottom, top]

  plt.imshow( data1, extent=extent, vmin=0.0, vmax=0.30 )
  # plt.imshow( data1, extent=extent )
  if type == 2:
    plt.yticks(np.linspace(0.0, 1.0, 6), np.linspace(2, 82, 6))

  plt.colorbar(label=r"$x_{\infty}^{MTAE} - x_{\infty}^{MTPE}$")
  if title:
    plt.title( title )
  plt.xlabel("$p$")
  plt.ylabel("$q$")
  plt.show()

def generateHeatMapRelative(filename1, filename2, title, type):
  data1 = []
  with open(filename1) as file:
    for line in file:
      data1.append([float(x) for x in line.split()])
  data2 = []
  with open(filename2) as file:
    for line in file:
      data2.append([float(x) for x in line.split()])

  for i in range(len(data1)):
    for j in range(len(data1[0])):
      data1[i][j] = (data1[i][j] - data2[i][j]) / data2[i][j]

  left = -0.0125
  right = 1.0125
  bottom = -0.0125
  top = 1.0125
  extent = [left, right, bottom, top]

  plt.imshow( data1, extent=extent, vmin=0.0, vmax=0.7 )
  # plt.imshow( data1, extent=extent )
  if type == 2:
    plt.yticks(np.linspace(0.0, 1.0, 6), np.linspace(2, 82, 6))

  plt.colorbar(label=r"$\frac{x_{\infty}^{MTAE} - x_{\infty}^{MTPE}}{x_{\infty}^{MTPE}}$")
  if title:
    plt.title( title )
  plt.xlabel("$p$")
  plt.ylabel("$q$")
  plt.show()

if __name__ == "__main__":
  generateHeatMap("mtae.txt", None, 1)
  generateHeatMap("mtpe.txt", None, 1)
  generateHeatMap("mtae2.txt", None, 2)
  generateHeatMap("mtpe2.txt", None, 2)
  generateHeatMap("mtae3.txt", None, 1)
  generateHeatMap("mtpe3.txt", None, 1)

  generateHeatMapDiff("mtae.txt", "mtpe.txt", None, 1)
  generateHeatMapRelative("mtae.txt", "mtpe.txt", None, 1)
  generateHeatMapDiff("mtae2.txt", "mtpe2.txt", None, 2)
  generateHeatMapRelative("mtae2.txt", "mtpe2.txt", None, 2)
  generateHeatMapDiff("mtae3.txt", "mtpe3.txt", None, 1)
  generateHeatMapRelative("mtae3.txt", "mtpe3.txt", None, 1)