import timeit

# NOTE: may need latest MPI from Microsoft: https://github.com/Microsoft/Microsoft-MPI

setup = """
from platypus import NSGAII, DTLZ2, PoolEvaluator
from platypus.mpipool import MPIPool

# simulate an computationally expensive problem
class DTLZ2_Slow(DTLZ2):
    
    def evaluate(self, solution):
        sum(range(1000000))
        super(DTLZ2_Slow, self).evaluate(solution)
"""

run = """
# define the problem definition
problem = DTLZ2_Slow()
pool = MPIPool()

# instantiate the optimization algorithm to run in parallel
with PoolEvaluator(pool) as evaluator:
    algorithm = NSGAII(problem, evaluator=evaluator)
    algorithm.run(10000)

pool.close()
"""

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=10))