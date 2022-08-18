import timeit

setup = """
from platypus import NSGAII, Problem, Real

def belegundu(vars):
    x = vars[0]
    y = vars[1]
    return [-2*x + y, 2*x + y], [-x + y - 1, x + y - 7]

problem = Problem(2, 2, 2)
problem.types[:] = [Real(0, 5), Real(0, 3)]
problem.constraints[:] = "<=0"
problem.function = belegundu
"""

run = "algorithm = NSGAII(problem); algorithm.run(1000)"

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=1000))