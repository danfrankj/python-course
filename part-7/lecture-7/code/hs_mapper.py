#!/usr/bin/env python
import sys


def mapper(key, value):
    # value is ignored, key is a line of text
    for word in key.split():
        yield word.strip(), 1

if __name__ == "__main__":
    for line in sys.stdin:
        keyval = line.split('\t')
        if len(keyval) > 1:
            key, val = (keyval[0], '\t'.join(keyval[1:]))
        else:
            key, val = (keyval[0], None)
        for outkey, outval in mapper(key, val):
            sys.stdout.write('%s\t%s\n' % (outkey, outval))
