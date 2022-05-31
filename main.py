from numpy import asarray
from numpy import argsort
from numpy.random import randn
from numpy.random import rand
import func


def in_range(point, p_range):
    result = True
    for i in range(len(p_range)):
        if point[i] < p_range[i, 0] or point[i] > p_range[i, 1]:
            result = False
    return result


def InitPopulation(lam, func_range):
    population = list()
    for i in range(lam):
        candidate = None
        while candidate is None or not in_range(candidate, func_range):
            candidate = func_range[:, 0] + rand(len(func_range)) * (func_range[:, 1] - func_range[:, 0])
        population.append(candidate)
    return population


# (mu, lambda) algorithm
def Evolution(function, func_range, epoch, step, mu, lam):
    best_individual, best_eval = None, 1e+10
    n_children = int(lam / mu)
    population = InitPopulation(lam, func_range)
    for epoch in range(epoch):
        fitness = [function(ind) for ind in population]
        ranks = argsort(argsort(fitness))
        selected = [i for i, _ in enumerate(ranks) if ranks[i] < mu]
        children = list()
        for i in selected:
            if fitness[i] < best_eval:
                best_individual, best_eval = population[i], fitness[i]
                print('%d, Best: f(%s) = %.5f' % (epoch, best_individual, best_eval))
            for _ in range(n_children):
                child = None
                while child is None or not in_range(child, func_range):
                    child = population[i] + randn(len(func_range)) * step
                children.append(child)
        population = children
    return [best_individual, best_eval]


def Start(function_number, e, s, m, l):
    min_range, max_range = -5.0, 5.0
    if function_number == 2:
        min_range, max_range = -15.0, -5.0
    if function_number == 3:
        min_range, max_range = -10.0, 10.0

    function = func.Ackley
    if function_number == 2:
        function = func.Bukina
    if function_number == 3:
        results = func.Holder

    function_range = asarray([[min_range, max_range], [min_range, max_range]])
    epoch = e
    step = s
    mu = m
    lam = l

    best, score = Evolution(function, function_range, epoch, step, mu, lam)
    print('Done!')
    print('f(%s) = %f' % (best, score))


function = 1
Start(function, 5000, 0.15, 20, 100)
func.show_function(function)
