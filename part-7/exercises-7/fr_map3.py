#!/usr/bin/env python
import sys

def mapper(key, value):
    yield key, value

if __name__ == "__main__":
    # input data format USER<TAB>FRIEND1, FRIEND2, FRIEND3
    for line in sys.stdin:
        key, val = line.strip().split('\t')
        for outkey, outval in mapper(key, val):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))