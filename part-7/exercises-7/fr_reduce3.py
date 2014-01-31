#!/usr/bin/env python
import sys
import numpy as np
from itertools import groupby, imap
from operator import itemgetter


def reducer(key, values):
    # key: edge; values: mutual
    values = [eval(v) for v in values]
    values = sorted(values, key=lambda x: x[1], reverse=True)
    yield key, values

if __name__ == "__main__":
    input = imap(lambda l: l.strip().split('\t'), sys.stdin)
    for key, val_gen in groupby(input, key=itemgetter(0)):
        vals = map(itemgetter(1), val_gen)
        for outkey, outval in reducer(key, vals):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))
