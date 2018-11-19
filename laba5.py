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
    Xi = 0.
    while i <= m:
        step = (start + (i - 1) * H) ** n
        Xi = Xi + step
        i = i + 1
    return Xi + 2


def SumOfYi():
    i = 1
    Yi = 0
    while i <= m:
        step = (start + (i - 1) * H)
        Yi = Yi + myFunction(step)
        i = i + 1
    return Yi - 4


def printTable (xi, fxi, pxi):
    i = 0
    for i in range(m):
        if i != 0:
            tmp = (pxi[i] - fxi[i])*100/fxi[i]
            print('%5.2f | %7.2f | %7.2f | %7.2f | %7.2f |' % (xi[i], fxi[i], pxi[i], pxi[i] - fxi[i], tmp))


def Alloc (n, arrayY, arrayX):
    i = 0
    j = 0
    while i < n:
        ind = i

        while j < n :
            if i == 0 and j == 0:
                arrayX[0][0] = m
            else:
                arrayX[i][j] = SumOfXi(ind)
            ind = ind + 1
            j = j + 1
        arrayY[i] = SumOfYi() * SumOfXi(i)
        i = i + 1
        j = 0
    answer = numpy.linalg.solve(arrayX, arrayY)
    return answer

#-------------------------------------------
arrayX = numpy.empty([4, 4])
arrayY = numpy.empty([4])
a = []
b = []
c = []
d = []
answer = Alloc(4, arrayY, arrayX)
t = numpy.linalg.lstsq(arrayX, arrayY, rcond=-1)
i = -1.
while (i < 3.):
    c.append(i)
    a.append(myFunction(i))
    b.append(answer[0] + answer[1]*i + answer[2]*i*i + answer[3]*i**3)
    d.append(t[0][0] + t[0][1]*i + t[0][2]*i*i + t[0][3]*i**3)
    i = i + 0.1
printTable(c, a, b)
plt.plot(c, a)
plt.plot(c, b)
# plt.plot(c, d)


#--------------------------------------------------------------------------
b = []
c = []
d = []
arrayX = numpy.empty([3, 3])
arrayY = numpy.empty([3])
answer = Alloc(3, arrayY, arrayX)
t = numpy.linalg.lstsq(arrayX, arrayY, rcond=-1)
i = -1.
while (i < 3.):
    c.append(i)
    d.append(answer[0] + answer[1]*i + answer[2]*i*i)
    b.append(t[0][0] + t[0][1]*i + t[0][2]*i*i)
    i = i + 0.1
printTable(c, a, b)
plt.plot(c, b)
#plt.plot(c, d)

#--------------------------------------------------------------------------
b = []
c = []
d = []
arrayX = numpy.empty([2, 2])
arrayY = numpy.empty([2])
answer = Alloc(2, arrayY, arrayX)
t = numpy.linalg.lstsq(arrayX, arrayY, rcond=-1)
i = -1.
while (i < 3.):
    c.append(i)
    d.append(answer[0] + answer[1]*i)
    b.append(t[0][0] + t[0][1]*i)
    i = i + 0.1
printTable(c, a, b)
plt.plot(c, b)
#plt.plot(c, d)

#--------------------------------------------------------------------------
b = []
c = []
d = []
arrayX = numpy.empty([1, 1])
arrayY = numpy.empty([1])
answer = Alloc(1, arrayY, arrayX)
t = numpy.linalg.lstsq(arrayX, arrayY, rcond=-1)
i = -1.
while (i < 3.):
    c.append(i)
    d.append(answer[0])
    b.append(t[0][0])
    i = i + 0.1
printTable(c, a, b)
plt.plot(c, b)
#plt.plot(c, d)

#--------------------------------------------------------------------------
b = []
c = []
d = []
i = -1.
while (i < 3.):
    c.append(i)
    d.append(i)
    b.append(i)
    i = i + 0.1
printTable(c, a, b)
plt.plot(c, b)
#plt.plot(c, d)






plt.show()
