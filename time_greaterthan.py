#!/usr/bin/env ipython3

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>

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