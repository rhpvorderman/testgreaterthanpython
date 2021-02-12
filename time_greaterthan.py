#!/usr/bin/env ipython3

import random

from IPython import get_ipython
ipython = get_ipython()

import numpy as np

integer_list = [random.randint(0, 99) for _ in range(100)]
integer_array = np.fromiter(integer_list, dtype=np.int_, count=100)
bool_list = [x > 30 for x in integer_list]
bool_array = np.fromiter(bool_list, dtype=np.bool_, count=100)

expressions = [
    "sum(1 for x in integer_list if x > 30)",
    "sum(x > 30 for x in integer_list)",
    "[x > 30 for x in integer_list].count(True)",
    "np.greater(integer_array, 30).sum()",
    "np.count_nonzero(np.greater(integer_array, 30))",
    "sum(bool_list)",
    "bool_list.count(True)",
    "np.sum(bool_array)",
    "bool_array.sum()",
    "np.count_nonzero(bool_array)",
]
for expr in expressions:
    print(expr)
    ipython.magic(f"timeit {expr}")
    print()