import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

def XInf(p, alpha, x0, y0):
  K = 2*p + alpha * (1 - p)

  if np.abs(K) < 1e-9:
    return np.nan

  ex = -(K * x0) - y0
  arg = -x0 * K * np.exp(ex)

  if arg < -1/np.e:
    return np.nan

  w = lambertw(arg).real

  return -w / K

def show(type):
  colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
  rang = np.linspace(0.0, 1.0, 1000)

  for ind, y0 in enumerate([0.0, 0.1, 0.25, 0.5, 0.75]):
    x0 = 1.0 - y0

    f = [XInf(p, type, x0, y0) for p in rang]
    plt.plot(rang, f, color=colors[ind], ls='-', lw=2, label=f"$y_0 = {y0}$")

  plt.legend(loc='upper right')
  plt.xlabel("$p$")
  plt.ylabel("$x_{\infty}$")
  plt.ylim(0, 1)
  plt.xlim(0, 1)
  plt.show()

if __name__ == "__main__":
  show(0)
  show(1)