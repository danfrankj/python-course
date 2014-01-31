#!/usr/bin/env python
import sys
from itertools import groupby, imap
from operator import itemgetter
import numpy as np


def reducer(key, values):
    if not np.any(np.array(values) == "ALREADYFRIENDS"):
        yield key[0], (key[1], len(values))
        yield key[1], (key[0], len(values))

if __name__ == "__main__":
    input = imap(lambda l: l.strip().split('\t'), sys.stdin)
    for key, val_gen in groupby(input, key=itemgetter(0)):
        vals = map(itemgetter(1), val_gen)
        for outkey, outval in reducer(eval(key), vals):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))
