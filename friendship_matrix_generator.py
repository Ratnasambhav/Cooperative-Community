from random import randint
import numpy

def generate(n):
    adj = [[0 for _ in range(0, n)] for _ in range(0, n)]
    for i in range(0, n):
        for j in range(0, i):
            adj[i][j] = adj[j][i] = randint(0, 1)
    return adj

a = generate(50)

def check_symmetric(a, tol=1e-8):
    return numpy.allclose(a, a.T, atol=tol)

print check_symmetric(numpy.array(a))
