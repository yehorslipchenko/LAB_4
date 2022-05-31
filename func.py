from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import sin
from numpy import e
from numpy import pi
from numpy import meshgrid
from numpy import fabs
from matplotlib import pyplot


def Ackley(ind):
    x, y = ind
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x ** 2 + y ** 2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


def Bukina(ind):
    x, y = ind
    return 100 * sqrt(fabs(y - 0.01 * pow(x, 2))) + 0.01 * fabs(x + 10)


def Holder(ind):
    x, y = ind
    return -fabs(sin(x) * cos(y) * exp(fabs(1 - (sqrt(pow(x, 2) + pow(y, 2)) / pi))))


def AckleyShow(x, y):
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x ** 2 + y ** 2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


def BukinaShow(x, y):
    return 100 * sqrt(fabs(y - 0.01 * pow(x, 2))) + 0.01 * fabs(x + 10)


def HolderShow(x, y):
    return -fabs(sin(x) * cos(y) * exp(fabs(1 - (sqrt(pow(x, 2) + pow(y, 2)) / pi))))


def show_function(function):
    r_min, r_max = 0, 0
    if function == 1:
        r_min, r_max = -5.0, 5.0
    if function == 2:
        r_min, r_max = -5.0, 5.0
    if function == 3:
        r_min, r_max = -10.0, 10.0
    if function != 1 and function != 2 and function != 3:
        return

    xaxis = arange(r_min, r_max, 0.1)
    yaxis = arange(r_min, r_max, 0.1)
    x, y = meshgrid(xaxis, yaxis)
    results = 0
    if function == 1:
        results = AckleyShow(x, y)
    if function == 2:
        results = BukinaShow(x, y)
    if function == 3:
        results = HolderShow(x, y)
    if function != 1 and function != 2 and function != 3:
        return
    figure = pyplot.figure()
    axis = figure.gca(projection='3d')
    axis.plot_surface(x, y, results, cmap='jet')
    pyplot.show()
