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


arrayX = numpy.array([[m, SumOfXi(1), SumOfXi(2), SumOfXi(3)], [SumOfXi(1), SumOfXi(2), SumOfXi(3), SumOfXi(4)],
                      [SumOfXi(2), SumOfXi(3), SumOfXi(4), SumOfXi(5)],
                      [SumOfXi(3), SumOfXi(4), SumOfXi(5), SumOfXi(6)]])
arrayY = numpy.array([SumOfYi(), SumOfXi(1) * SumOfYi(), SumOfXi(2) * SumOfYi(), SumOfXi(3) * SumOfYi()])
answer = numpy.linalg.solve(arrayX, arrayY)

s = (answer[0] + answer[1] + answer[2] + answer[3]) * 2

t = numpy.linalg.lstsq(arrayX, arrayY, rcond=-1)

print(t[0][1])
print(answer[1])
# print(s)
# print(myFunction(2))


a = []
b = []
c = []
d = []
i = 1
for i in range(m):
    c.append(start + (i - 1) * H)
    a.append(myFunction(c[i - 1]))
    b.append((answer[0] + answer[1] + answer[2] + answer[3]) * c[i - 1])
    d.append((t[0][0] + t[0][1] + t[0][2] + t[0][3]) * c[i - 1])
    i = i + 1

plt.plot(c, a)
plt.plot(c, b)
plt.plot(c, d)
plt.show()
