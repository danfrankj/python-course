#!/usr/bin/env python
from __future__ import print_function
import sys
import importlib


TESTS = []

def grade(path):
    sys.path.append(path)
    hw1 = importlib.import_module('hw-1')

    init_arith_tests()
    init_str_tests()
    init_math_tests()
    func_table = {'arith2': hw1.arith2,
                  'arith3': hw1.arith3,
                  'arith4': hw1.arith4,
                  'str2': hw1.str2,
                  'str3': hw1.str3,
                  'str4': hw1.str4,
                  'seq_add': hw1.seq_add,
                  'fact': hw1.fact}
    total_tests = 0
    successes = 0
    for test in TESTS:
        if run_test(func_table, **test):
            successes += 1
            total_tests += 1

    print('\n%d / %d correct (%f)' % (successes, total_tests,
                                      float(successes) / total_tests))

    score = successes
    PF = "PASS" if float(successes) / total_tests > .7 else "FAIL"
    return score, PF


def create_test(i, name, input, output, type):
    TESTS.append({'i': i, 'name': name, 'input': input, 'output': output,
                  'type': type})

def init_arith_tests():
    create_test(1, 'arith2', {'x': 5, 'y': 4}, 14, 'arith')
    create_test(2, 'arith2', {'x': 9, 'y': 10}, 37, 'arith')
    create_test(3, 'arith2', {'x': 2, 'y': 2}, 12, 'arith')
    create_test(4, 'arith3', {'x': 5, 'y': 4, 'z': 4}, 0, 'arith')
    create_test(5, 'arith3', {'x': 4, 'y': 4, 'z': 4}, 0, 'arith')
    create_test(6, 'arith3', {'x': 4, 'y': 4, 'z': 5}, 0, 'arith')
    create_test(7, 'arith3', {'x': 4, 'y': 5, 'z': 4}, 0, 'arith')
    create_test(8, 'arith3', {'x': 1, 'y': 2, 'z': 3}, 1, 'arith')
    create_test(9, 'arith3', {'x': -1, 'y': 2, 'z': 3}, 1, 'arith')
    create_test(10, 'arith3', {'x': 4, 'y': 3, 'z': 2}, 2, 'arith')
    create_test(11, 'arith3', {'x': 1, 'y': 2, 'z': 0}, 2, 'arith')
    create_test(12, 'arith4', {'x': 1, 'y': 2, 'z': 0, 'w': 10}, 37, 'arith')
    create_test(13, 'arith4', {'x': 0, 'y': 0, 'z': 0, 'w': 12}, 10, 'arith')
    create_test(14, 'arith4', {'x': 1, 'y': 1, 'z': 0, 'w': 12}, 10, 'arith')

def init_str_tests():
    create_test(1, 'str2', {'a': 'zz', 'b': 'yy'}, 'zzyyyyyyzz', 'str')
    create_test(2, 'str2', {'a': 'zz', 'b': 'y'}, 'zzyyyzz', 'str')
    create_test(3, 'str2', {'a': '', 'b': 'hi'}, 'hihihi', 'str')
    create_test(4, 'str3', {'a': '1', 'b': '2', 'c': '3'}, '123123', 'str')
    create_test(5, 'str3', {'a': '', 'b': '2', 'c': '3'}, '2323', 'str')
    create_test(6, 'str4', {'a': 'foo', 'b': 'garply', 'c': 'bar', 'd': 'baz'},
                'foogarply', 'str')
    create_test(7, 'str4', {'a': 'foo', 'b': 'garply', 'c': 'bar', 'd': 'bazz'},
                'garplygarplybarbar', 'str')
    create_test(8, 'str4', {'a': '', 'b': 'garply', 'c': '', 'd': ''},
                'garply', 'str')

def init_math_tests():
    create_test(1, 'seq_add', {'start': 1, 'end': 10, 'k': 3}, 22, 'math')
    create_test(2, 'seq_add', {'start': 1, 'end': 5, 'k': 6}, 1, 'math')
    create_test(3, 'seq_add', {'start': 4, 'end': 9, 'k': 2}, 18, 'math')
    create_test(4, 'seq_add', {'start': 7, 'end': 7, 'k': 3}, 7, 'math')
    create_test(5, 'seq_add', {'start': -4, 'end': 8, 'k': 5}, 3, 'math')
    create_test(6, 'seq_add', {'start': -5, 'end': 0, 'k': 1}, -15, 'math')
    create_test(7, 'fact', {'n': 5}, 120, 'math')
    create_test(8, 'fact', {'n': -1}, 0, 'math')

def run_test(func_table, i, name, input, output, type):
    print('\n running %s test %d...' % (type, i))
    try:
        result = func_table[name](**input)
    except:
        print('\tFAILED (could not execute function %s) ' % name)
        return False

    if result != output:
        print('\tFAILED\n\t\tInput was: %s' % str(input))
        print('\t\tExpected result: %s' % str(output))
        print('\t\tActual result: %s' % str(result))
        return False

    print('\tSUCCESS')
    return True


