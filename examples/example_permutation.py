import timeit

setup = """
from platypus import GeneticAlgorithm, Problem, Permutation, nondominated, unique

def ordering(x):
    # x[0] is the permutation, this calculates the difference between the permutation and an ordered list
    return sum([abs(p_i - i) for i, p_i in enumerate(x[0])])

problem = Problem(1, 1)
problem.types[0] = Permutation(range(10)) # Permutation of elements [0, 1, ..., 9]
problem.function = ordering
"""

run = "algorithm = GeneticAlgorithm(problem); algorithm.run(1000)"

print("The time of execution of above program is :",
      timeit.timeit(setup=setup,
                    stmt=run,
                    number=1000))