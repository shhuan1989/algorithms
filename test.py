#!/bin/python

import math
import os
import random
import re
import sys

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
# cmap = cm.get_cmap('Blues')

# w = np.random.rand(2, 1)
w0 = np.array([0.6, 0.2])
b0 = 0.1

points = np.random.rand(20, 2)
x = np.linspace(0, 1, 20).reshape(-1, 1)
x = np.concatenate([x, np.ones_like(x)], axis=1)
x[:, 0]
y = x.dot(w0)+b0
plt.plot(x[:,0], y)


w = (y[1]-y[0]) / (x[1, 0] - x[0, 0])
b = y[0] - w*x[0, 0]
w, b

cat = [1 if x > 0 else 0 for x in points[:, 1] - (w*points[:, 0] + b)]

colors = ['r' if x > 0 else 'g' for x in cat]
plt.scatter(x=points[:, 0], y=points[:, 1], c=cat)
# print(cmap(0), cmap(1))
print(x)
print(y)
plt.show()


print(points.dot(np.array([w, b]).reshape(-1, 1)))


w = np.random.rand(3, 1)
y = np.array([1 if v == 1 else -1 for v in cat]).reshape(-1, 1)
print(y)
print(x.shape, y.shape, w.shape)
alpha = 0.01
N = len(y)
costs = []
x = np.c_[-points[:, 0], [-1]*len(points), points[:, 1]]
for epoch in range(1000):
    cost = 0.0
    for i in range(len(y)):
        rand_ind = np.random.randint(0, N)
        xi = x[rand_ind].reshape(1, -1)
        yi = y[rand_ind].reshape(1, 1)
        yhat = np.sum(np.sign(xi.dot(w)))
        yi = np.sum(yi)
        cost += 1.0 / 2 / N * (1-yi*yhat) ** 2
        a = (1-yi * yhat) * yi
        w = w + 1.0 / N * alpha * a * (xi.reshape(-1, 1))
        w[-1, 0] = 1
    
    costs.append(cost)
        
print(w)
print(costs[-1])


plt.plot([i for i in range(len(costs))], costs)
plt.show()

# print(np.sign(x[:, 1].reshape(-1, 1) - np.stack([x[:, 0], np.ones((len(x),))], axis=1).dot(w)))
# print(np.sign(y))
yhat = np.sign(x.dot(w))
# print(np.sum(np.square(1-y*yhat)))
print(np.c_[yhat, y])
plt.scatter(x=-x[:, 0], y=x[:, 2], c=[1 if v > 0 else 0 for v in y.flatten()])
# plt.plot([i for i in range(len(costs))], costs)
plt.show()