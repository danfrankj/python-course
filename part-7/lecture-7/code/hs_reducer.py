#!/usr/bin/env python
import sys
from itertools import groupby, imap
from operator import itemgetter

def reducer(key, values):
    # key: word; values: list of 1's
    yield key, sum([int(v) for v in values])

if __name__ == "__main__":
    input = imap(lambda l: l.strip().split('\t'), sys.stdin)
    for key, val_gen in groupby(input, key=itemgetter(0)):
        vals = map(itemgetter(1), val_gen)
        for outkey, outval in reducer(key, vals):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))
