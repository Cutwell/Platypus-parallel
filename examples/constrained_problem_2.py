import timeit

setup = """
from platypus import NSGAII, Problem, Real

class Belegundu(Problem):

    def __init__(self):
        super(Belegundu, self).__init__(2, 2, 2)
        self.types[:] = [Real(0, 5), Real(0, 3)]
        self.constraints[:] = "<=0"
    
    def evaluate(self, solution):
        x = solution.variables[0]
        y = solution.variables[1]
        solution.objectives[:] = [-2*x + y, 2*x + y]
        solution.constraints[:] = [-x + y - 1, x + y - 7]
"""

run = "algorithm = NSGAII(Belegundu()); algorithm.run(1000)"

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=1000))