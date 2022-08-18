# Platypus-Parallel

<a href="https://github.com/Cutwell/Platypus-parallel"><img alt="GitHub Actions status" src="https://github.com/Cutwell/Platypus-parallel/workflows/Tests/badge.svg?branch=master&event=push"></a>
[![Documentation Status](https://readthedocs.org/projects/platypus/badge/?version=latest)](http://platypus.readthedocs.org/en/latest/?badge=latest)

## What's new?
* Offspring generation and evaluation is parallelized using `asyncio` library, speeding up execution.
* Acts as a drop-in replacement to existing `Platypus-Opt` projects.

## What is Platypus?

Platypus is a framework for evolutionary computing in Python with a focus on
multiobjective evolutionary algorithms (MOEAs).  It differs from existing
optimization libraries, including PyGMO, Inspyred, DEAP, and Scipy, by providing
optimization algorithms and analysis tools for multiobjective optimization.
It currently supports NSGA-II, NSGA-III, MOEA/D, IBEA, Epsilon-MOEA, SPEA2, GDE3,
OMOPSO, SMPSO, and Epsilon-NSGA-II.  For more information, see our
[IPython Notebook](https://gist.github.com/dhadka/ba6d3c570400bdb411c3)
or our [online documentation](http://platypus.readthedocs.org/en/latest/index.html).

## Speed-up

Speed-up is build into testing: there's no purpose in parallization if it has no tangible benefit.

| Problem | Example | `platypus-opt` timeit | `platypus-opt-parallel` timeit | speed-up (seconds / % speed-up) |
|:---:|:---:|:---:|:---:|:---:|
|  |  |  |  |  |

## Installation

To install the latest development version of Platypus, run the following commands:

```
    git clone https://github.com/Project-Platypus/Platypus.git
    cd Platypus
    python setup.py install
```

## License

Platypus is released under the GNU General Public License.
