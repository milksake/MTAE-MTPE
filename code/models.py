import numpy as np
import random

def MTGraphs(graph, lamb, alpha, tend, numIni):
  # initialize state
  I=[len(graph)-numIni]
  S=[numIni]
  R=[0]
  t=[0]
  state = [0]*len(graph)
  numIgnorants = [0]*len(graph)

  for i in range(len(graph)):
    numIgnorants[i] = len(graph[i])

  spreaders = []
  for i in range(numIni):
    while True:
      indInf = random.randint(0, len(graph)-1)
      if state[indInf] == 0:
        break
    state[indInf] = 1
    spreaders.append(indInf)
    for v in graph[indInf]:
      numIgnorants[v] -= 1

  def propagate(u):
    spreaders.append(u)
    S[-1] += 1
    I[-1] -= 1
    state[u] = 1
    for v in graph[u]:
      numIgnorants[v] -= 1

  def stifle(u):
    spreaders.remove(u)
    S[-1] -= 1
    R[-1] += 1
    state[u] = 2

  events = [
      propagate,     # propagation
      stifle,     # stifling
  ]

  while (t[-1] < tend and S[-1] > 0):
    # choose spreader
    prob = []
    sumProb = 0
    for i in spreaders:
      prob.append(numIgnorants[i]*lamb + alpha*(len(graph[i]) - numIgnorants[i]))
      sumProb += prob[-1]
    if sumProb == 0:
      break
    prob = np.array(prob) / sumProb
    spreader = random.choices(range(len(prob)), weights=prob)
    spreader = spreaders[spreader[0]]

    # calculate process probabilities for current state
    a = np.array([
        lamb*numIgnorants[spreader],
        alpha*(len(graph[spreader]) - numIgnorants[spreader])
    ])

    suma = sum(a)

    # update time
    t.append(t[-1]+1)

    a = a / suma
    rand = random.choices(range(len(a)), weights=a)

    # update states
    I.append(I[-1])
    S.append(S[-1])
    R.append(R[-1])

    #print(spreaders)
    #print(I)
    #print(S)
    #print(R)

    if rand[0] == 0:
      ignorantInd = random.randint(0, numIgnorants[spreader]-1)
      i = 0
      ignorant = 0
      for j in graph[spreader]:
        if state[j] == 0:
          if i == ignorantInd:
            ignorant = j
            break
          i += 1
      events[rand[0]](ignorant)
    else:
      events[rand[0]](spreader)

  return (t, I, S, R)

def MTPEGraphs(graph, lamb, alpha, p, tend, numIni):
  # initialize state
  I=[len(graph)-numIni]
  S=[numIni]
  R=[0]
  t=[0]
  state = [0]*len(graph)
  numIgnorants = [0]*len(graph)

  for i in range(len(graph)):
    numIgnorants[i] = len(graph[i])

  spreaders = []
  for i in range(numIni):
    while True:
      indInf = random.randint(0, len(graph)-1)
      if state[indInf] == 0:
        break
    state[indInf] = 1
    spreaders.append(indInf)
    for v in graph[indInf]:
      numIgnorants[v] -= 1

  def propagate(u):
    spreaders.append(u)
    I[-1] -= 1
    S[-1] += 1
    state[u] = 1
    for v in graph[u]:
      numIgnorants[v] -= 1

  def stifle1(u):
    spreaders.remove(u)
    S[-1] -= 1
    R[-1] += 1
    state[u] = 2

  def stifle2(u):
    I[-1] -= 1
    R[-1] += 1
    state[u] = 2
    for v in graph[u]:
      numIgnorants[v] -= 1

  while (t[-1] < tend and S[-1] > 0):
    # choose spreader
    prob = []
    sumProb = 0
    for i in spreaders:
      prob.append(numIgnorants[i]*lamb + alpha*(len(graph[i]) - numIgnorants[i]))
      sumProb += prob[-1]
    if sumProb == 0:
      break
    prob = np.array(prob) / sumProb
    spreader = random.choices(range(len(prob)), weights=prob)
    spreader = spreaders[spreader[0]]

    # calculate process probabilities for current state
    a = np.array([
        lamb*numIgnorants[spreader],
        alpha*(len(graph[spreader]) - numIgnorants[spreader])
    ])

    suma = sum(a)

    # update time
    t.append(t[-1]+1)

    a = a / suma
    rand = random.choices(range(len(a)), weights=a)

    # update states
    I.append(I[-1])
    S.append(S[-1])
    R.append(R[-1])

    #print(spreaders)
    #print(I)
    #print(S)
    #print(R)

    if rand[0] == 0:
      ignorantInd = random.randint(0, numIgnorants[spreader]-1)
      i = 0
      ignorant = 0
      for j in graph[spreader]:
        if state[j] == 0:
          if i == ignorantInd:
            ignorant = j
            break
          i += 1
      val = random.random()
      if val < p:
        propagate(ignorant)
      else:
        stifle2(ignorant)
    else:
      stifle1(spreader)

  return (t, I, S, R)

def MTAEGraphs(graph, lamb, alpha, p, tend, numIni):
  # initialize state
  I=[len(graph)-numIni]
  S=[numIni]
  R=[0]
  t=[0]
  state = [0]*len(graph)
  numIgnorants = [0]*len(graph)

  for i in range(len(graph)):
    numIgnorants[i] = len(graph[i])

  spreaders = []
  for i in range(numIni):
    while True:
      indInf = random.randint(0, len(graph)-1)
      if state[indInf] == 0:
        break
    state[indInf] = 1
    spreaders.append(indInf)
    for v in graph[indInf]:
      numIgnorants[v] -= 1

  def propagate(u):
    spreaders.append(u)
    I[-1] -= 1
    S[-1] += 1
    state[u] = 1
    for v in graph[u]:
      numIgnorants[v] -= 1

  def stifle1(u):
    spreaders.remove(u)
    S[-1] -= 1
    R[-1] += 1
    state[u] = 2

  def stifle2(u):
    I[-1] -= 1
    R[-1] += 1
    state[u] = 2
    for v in graph[u]:
      numIgnorants[v] -= 1

  while (t[-1] < tend and S[-1] > 0):
    # choose spreader
    prob = []
    sumProb = 0
    for i in spreaders:
      prob.append(numIgnorants[i]*lamb + alpha*(len(graph[i]) - numIgnorants[i]))
      sumProb += prob[-1]
    # print(I[-1], S[-1], R[-1], prob, sumProb)
    if sumProb == 0:
      break
    prob = np.array(prob) / sumProb
    spreader = random.choices(range(len(prob)), weights=prob)
    spreader = spreaders[spreader[0]]

    # calculate process probabilities for current state
    a = np.array([
        lamb*numIgnorants[spreader],
        alpha*(len(graph[spreader]) - numIgnorants[spreader])
    ])

    suma = sum(a)

    # update time
    t.append(t[-1]+1)

    a = a / suma
    rand = random.choices(range(len(a)), weights=a)

    # update states
    I.append(I[-1])
    S.append(S[-1])
    R.append(R[-1])

    #print(spreaders)
    #print(I)
    #print(S)
    #print(R)

    if rand[0] == 0:
      ignorantInd = random.randint(0, numIgnorants[spreader]-1)
      i = 0
      ignorant = 0
      for j in graph[spreader]:
        if state[j] == 0:
          if i == ignorantInd:
            ignorant = j
            break
          i += 1
      val = random.random()
      if val < p:
        propagate(ignorant)
      else:
        stifle1(spreader)
        stifle2(ignorant)
    else:
      stifle1(spreader)

  return (t, I, S, R)