#!/usr/bin/env python
import sys

def mapper2(key, value):
    for v1 in value:
        for v2 in value:
            if v2 <= v1:
                continue
            yield (v1, v2), key

    for v in value:
        outkey = tuple(sorted((key, v)))
        yield outkey, "ALREADYFRIENDS"


if __name__ == "__main__":
    for line in sys.stdin:
        key, val = line.split('\t')
        for outkey, outval in mapper2(key, eval(val)):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))