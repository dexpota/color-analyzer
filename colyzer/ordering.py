#!/urs/bin/env python3

import sys
import colorsys

def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=lambda _: seq[2])

def hex_to_rgb(h):
    h = h.lstrip('#')
    hlen = len(h)
    return tuple(int(h[int(i):int(i+hlen/3)], 16) for i in range(0, hlen, int(hlen/3)))

couples = []

for line in sys.stdin.readlines():
    key, value = line.split()
    rgb=hex_to_rgb(value)
    couples.append((key, rgb, colorsys.rgb_to_hsv(*rgb)))

print(couples)

hsv_ordering=argsort(couples)

colours_length=len(couples)

from scipy.spatial import distance
import numpy as np
# Distance matrix
A = np.zeros([colours_length,colours_length])
for x in range(0, colours_length-1):
    for y in range(0, colours_length-1):
        A[x,y] = distance.euclidean(couples[x][1], couples[y][1])

print(A)

from nn import NN
# Nearest neighbour algorithm
path, _ = NN(A, 0)

import svgwrite

dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

path = hsv_ordering

# Final array
colours_nn = []
x=0
for i in path:
    x=x+10
    dwg.add(dwg.rect((x, 0), (10, 10), fill=svgwrite.rgb(*couples[i][1])))
    print(  couples[i]  )
dwg.save()
