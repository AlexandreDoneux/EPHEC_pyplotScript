from matplotlib import pyplot

x = [1, 3, 2, 4, 2, 3, 1]
y = [2, 2, 4, 5, 1, 6, 3]

ax = pyplot.plot(x, y, 'ro--')
pyplot.plot(y, x, color = "green", linestyle= ":", marker= "+", markersize= 5)

#pyplot.xlim(0, 5)
#pyplot.xlim(0, 3)


pyplot.show()