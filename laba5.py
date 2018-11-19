import math
import numpy
import matplotlib.pyplot as plt

start = -1
end = 3
H = (end - start) / 10
m = 11
Pn = [0, 0, 0, 0]


def myFunction(x):
    y = (1 + x) * math.e ** (-2 * x)
    return y


def SumOfXi(n):
    i = 1
    Xi = 0
    while i < m:
        Xi = Xi + (start + (i - 1) * H) ** n
        i = i + 1
    return Xi


def SumOfYi():
    i = 1
    Yi = 0
    for i in range(m):
        Yi = Yi + myFunction(start + (i - 1) * H)
        i = i + 1
    return Yi


def printTable (xi, fxi, pxi):
    i = 0
    for i in range(m):
        tmp = (pxi[i] - fxi[i])*100/fxi[i]
        print('%5.2f | %7.2f | %7.2f | %7.2f | %7.2f |' % (xi[i], fxi[i], pxi[i], pxi[i] - fxi[i], tmp))

def Alloc (n, arrayY, arrayX):
    answer = numpy.array()
    i = 1
    j= 0
    arrayX[0][0] = m
    ind = 1
    for i in range(n):
        for j in range(n):
            arrayX[i][j] = SumOfXi(ind)
            ind = ind + 1
        arrayY[j] = SumOfYi()*SumOfXi(ind)
        ind = j + 1

    answer = numpy.linalg.solve(arrayX, arrayY)
    return answer



arrayX = []
arrayY =[]
n = 4
answer = Alloc(n, arrayY, arrayX)

# t = numpy.linalg.lstsq(arrayX, arrayY, rcond=-1)

a = []
b = []
c = []
d = []
i = -1.
while( i < 3.):
    c.append(i)
    a.append(myFunction(i))
    b.append((answer[0] + answer[1] + answer[2] + answer[3]) * i)
    i = i + 0.1

printTable(c, a, b)



plt.plot(c, a)
plt.plot(c, b)
plt.plot(c, d)
plt.show()
