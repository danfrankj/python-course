#!/usr/bin/env python
import sys

def mapper(key, value):
    yield key, value
    yield value, key

if __name__ == "__main__":
    """ input data format USER1<TAB>USER2 """
    for line in sys.stdin:
        key, val = line.strip().split('\t')
        for outkey, outval in mapper(key, val):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))