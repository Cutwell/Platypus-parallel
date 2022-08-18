import unittest
import timeit

class TestSpeedup(unittest.TestCase):

    def test1(self):
        

        # get original platypus speed
        setup = """
from platypus.tests.platypus import NSGAII, Problem, Real

def belegundu(vars):
    x = vars[0]
    y = vars[1]
    return [-2*x + y, 2*x + y], [-x + y - 1, x + y - 7]

problem = Problem(2, 2, 2)
problem.types[:] = [Real(0, 5), Real(0, 3)]
problem.constraints[:] = "<=0"
problem.function = belegundu
"""

        run = "algorithm = NSGAII(problem, population_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
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

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance
    
    def test2(self):
        # get original platypus speed
        setup = """
from platypus.tests.platypus import NSGAII, Problem, Real

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

        run = "algorithm = NSGAII(Belegundu(), population_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
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

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance
    
    def test3(self):
        # get original platypus speed
        setup = """
from platypus.tests.platypus import NSGAII, Problem, Real

def schaffer(x):
    return [x[0]**2, (x[0]-2)**2]

problem = Problem(1, 2)
problem.types[:] = Real(-10, 10)
problem.function = schaffer
"""

        run = "algorithm = NSGAII(problem, population_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
        setup = """
from platypus import NSGAII, Problem, Real

def schaffer(x):
    return [x[0]**2, (x[0]-2)**2]

problem = Problem(1, 2)
problem.types[:] = Real(-10, 10)
problem.function = schaffer
"""

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance
    
    def test4(self):
        # get original platypus speed
        setup = """
from platypus.tests.platypus import NSGAII, Problem, Real

class Schaffer(Problem):

    def __init__(self):
        super(Schaffer, self).__init__(1, 2)
        self.types[:] = Real(-10, 10)
    
    def evaluate(self, solution):
        x = solution.variables[:]
        solution.objectives[:] = [x[0]**2, (x[0]-2)**2]
"""

        run = "algorithm = NSGAII(Schaffer(), population_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
        setup = """
from platypus import NSGAII, Problem, Real

class Schaffer(Problem):

    def __init__(self):
        super(Schaffer, self).__init__(1, 2)
        self.types[:] = Real(-10, 10)
    
    def evaluate(self, solution):
        x = solution.variables[:]
        solution.objectives[:] = [x[0]**2, (x[0]-2)**2]
"""

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance
    
    def test5(self):
        # get original platypus speed
        setup = """
from platypus.tests.platypus import GeneticAlgorithm, Problem, Permutation

def ordering(x):
    # x[0] is the permutation, this calculates the difference between the permutation and an ordered list
    return sum([abs(p_i - i) for i, p_i in enumerate(x[0])])

problem = Problem(1, 1)
problem.types[0] = Permutation(range(10)) # Permutation of elements [0, 1, ..., 9]
problem.function = ordering
"""

        run = "algorithm = GeneticAlgorithm(problem, population_size=1000, offspring_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
        setup = """
from platypus import GeneticAlgorithm, Problem, Permutation

def ordering(x):
    # x[0] is the permutation, this calculates the difference between the permutation and an ordered list
    return sum([abs(p_i - i) for i, p_i in enumerate(x[0])])

problem = Problem(1, 1)
problem.types[0] = Permutation(range(10)) # Permutation of elements [0, 1, ..., 9]
problem.function = ordering
"""

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance
    
    def test6(self):
        # get original platypus speed
        setup = """
from platypus.tests.platypus import NSGAII, DTLZ2

# define the problem definition
problem = DTLZ2()
"""

        run = "algorithm = NSGAII(problem, population_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
        setup = """
from platypus import NSGAII, DTLZ2

# define the problem definition
problem = DTLZ2()
"""

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance
    
    def test7(self):
        # get original platypus speed
        setup = """
import math
from platypus.tests.platypus import GeneticAlgorithm, Problem, Permutation

# The (x, y) coordinates of cities in the PR76 instance.  This instance has
# an optimal tour length of 108159.
cities = [(3600, 2300), (3100, 3300), (4700, 5750), (5400, 5750), (5608, 7103),
        (4493, 7102), (3600, 6950), (3100, 7250), (4700, 8450), (5400, 8450),
        (5610, 10053), (4492, 10052), (3600, 10800), (3100, 10950), (4700, 11650),
        (5400, 11650), (6650, 10800), (7300, 10950), (7300, 7250), (6650, 6950),
        (7300, 3300), (6650, 2300), (5400, 1600), (8350, 2300), (7850, 3300),
        (9450, 5750), (10150, 5750), (10358, 7103), (9243, 7102), (8350, 6950),
        (7850, 7250), (9450, 8450), (10150, 8450), (10360, 10053), (9242, 10052),
        (8350, 10800), (7850, 10950), (9450, 11650), (10150, 11650), (11400, 10800),
        (12050, 10950), (12050, 7250), (11400, 6950), (12050, 3300), (11400, 2300),
        (10150, 1600), (13100, 2300), (12600, 3300), (14200, 5750), (14900, 5750),
        (15108, 7103), (13993, 7102), (13100, 6950), (12600, 7250), (14200, 8450),
        (14900, 8450), (15110, 10053), (13992, 10052), (13100, 10800), (12600, 10950),
        (14200, 11650), (14900, 11650), (16150, 10800), (16800, 10950), (16800, 7250),
        (16150, 6950), (16800, 3300), (16150, 2300), (14900, 1600), (19800, 800),
        (19800, 1000), (19800, 11900), (19800, 12200), (200, 12200), (200, 1100),
        (200, 800)]

def dist(x, y):
    return round(math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2))
    
def tsp(x):
    tour = x[0]
    return sum([dist(cities[tour[i]], cities[tour[(i + 1) % len(cities)]]) for i in range(len(tour))])

problem = Problem(1, 1)
problem.types[0] = Permutation(range(len(cities)))
problem.directions[0] = Problem.MINIMIZE
problem.function = tsp
"""

        run = "algorithm = GeneticAlgorithm(problem, population_size=1000, offspring_size=1000); algorithm.run(1000)"

        og = self._timeit(setup, run)

        # get parallelized speedup
        setup = """
import math
from platypus import GeneticAlgorithm, Problem, Permutation

# The (x, y) coordinates of cities in the PR76 instance.  This instance has
# an optimal tour length of 108159.
cities = [(3600, 2300), (3100, 3300), (4700, 5750), (5400, 5750), (5608, 7103),
        (4493, 7102), (3600, 6950), (3100, 7250), (4700, 8450), (5400, 8450),
        (5610, 10053), (4492, 10052), (3600, 10800), (3100, 10950), (4700, 11650),
        (5400, 11650), (6650, 10800), (7300, 10950), (7300, 7250), (6650, 6950),
        (7300, 3300), (6650, 2300), (5400, 1600), (8350, 2300), (7850, 3300),
        (9450, 5750), (10150, 5750), (10358, 7103), (9243, 7102), (8350, 6950),
        (7850, 7250), (9450, 8450), (10150, 8450), (10360, 10053), (9242, 10052),
        (8350, 10800), (7850, 10950), (9450, 11650), (10150, 11650), (11400, 10800),
        (12050, 10950), (12050, 7250), (11400, 6950), (12050, 3300), (11400, 2300),
        (10150, 1600), (13100, 2300), (12600, 3300), (14200, 5750), (14900, 5750),
        (15108, 7103), (13993, 7102), (13100, 6950), (12600, 7250), (14200, 8450),
        (14900, 8450), (15110, 10053), (13992, 10052), (13100, 10800), (12600, 10950),
        (14200, 11650), (14900, 11650), (16150, 10800), (16800, 10950), (16800, 7250),
        (16150, 6950), (16800, 3300), (16150, 2300), (14900, 1600), (19800, 800),
        (19800, 1000), (19800, 11900), (19800, 12200), (200, 12200), (200, 1100),
        (200, 800)]

def dist(x, y):
    return round(math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2))
    
def tsp(x):
    tour = x[0]
    return sum([dist(cities[tour[i]], cities[tour[(i + 1) % len(cities)]]) for i in range(len(tour))])

problem = Problem(1, 1)
problem.types[0] = Permutation(range(len(cities)))
problem.directions[0] = Problem.MINIMIZE
problem.function = tsp
"""

        new = self._timeit(setup, run)

        assert og >= new    # assert speedup is at least equal to original performance

    def _timeit(self, setup, run):
        return timeit.timeit(setup=setup,
                    stmt=run,
                    number=10)
