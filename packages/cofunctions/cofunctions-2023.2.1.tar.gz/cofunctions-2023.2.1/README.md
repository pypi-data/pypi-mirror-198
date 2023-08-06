cofunctions: Simple coroutines for Python
=========================================

To create a cofunction, write a generator with the ``@cofunction`` decorator
and ``yield`` a function that does your processing.

Example of a function that accumulates a sum:

```py
from cofunctions import cofunction
from math import exp, log

@cofunction
def logsumexp(initial=0.):
    '''log-sum-exp example (does not actually prevent overflow)'''
    sum = initial

    # this function gathers the inputs
    def _(x):
        nonlocal sum  # important for changing values
        sum += exp(x)
        return sum

    yield _

    # do additional processing here

    result = log(sum)

    return result

# create the cofunction
lse = logsumexp()

# call the cofunction to do processing
partial1 = lse(1)
partial2 = lse(2)
partial3 = lse(3)

# finish the cofunction to run the additional processing
result = lse.finish()

print(partial1, partial2, partial3)
# 2.718281828459045 10.107337927389695 30.19287485057736
print(result)
# 3.40760596444438
```
