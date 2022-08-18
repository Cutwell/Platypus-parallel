import timeit

setup = """
from platypus import NSGAII, DTLZ2

# define the problem definition
problem = DTLZ2()
"""

run = "algorithm = NSGAII(problem); algorithm.run(1000)"

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=1000))