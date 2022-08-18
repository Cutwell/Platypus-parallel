import timeit

setup = """
from platypus import NSGAII, DTLZ2, ProcessPoolEvaluator

# simulate an computationally expensive problem
class DTLZ2_Slow(DTLZ2):
    
    def evaluate(self, solution):
        sum(range(1000000))
        super(DTLZ2_Slow, self).evaluate(solution)
"""

run = """
# define the problem definition
problem = DTLZ2_Slow()

# instantiate the optimization algorithm to run in parallel
with ProcessPoolEvaluator(4) as evaluator:
    algorithm = NSGAII(problem, evaluator=evaluator)
    algorithm.run(10000)
"""

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=10))