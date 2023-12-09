from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re

import hashlib

data = "iwrupvqb"

for i in it.count():
    if hashlib.md5((data + str(i)).encode()).hexdigest().startswith("00000"):
        print(i)
        break

for i in it.count():
    if hashlib.md5((data + str(i)).encode()).hexdigest().startswith("000000"):
        print(i)
        break
