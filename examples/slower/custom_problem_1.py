import timeit

setup = """
from platypus import NSGAII, Problem, Real

def schaffer(x):
    return [x[0]**2, (x[0]-2)**2]

problem = Problem(1, 2)
problem.types[:] = Real(-10, 10)
problem.function = schaffer
"""

run = "algorithm = NSGAII(problem); algorithm.run(1000)"

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=1000))