import sys
import math
import coordinates_tuples
import coordinates_dicts

'''
TEST DRIVER

DO NOT MODIFY

USAGE:

python grader.py [type] [number]

type is either 'tuples' or 'dicts' to specify running a test on the
implementation in coordinates_tuples or coordinates_dicts

number is the test number (1, 2, ..., 10).

If you do not provide any arguments, the script will execute all tests
for both the tuples and dicts implementation.

If type is provided but the test number is not, all tests of that type
will run.

Examples:

python grader.py
python grader.py tuples
python grader.py tuples 4
python grader.py dicts
python grader.py dicts 3

These calls will run (1) all tests, (2) all tuples tests, (3) the fourth
tuples test, (4) all dicts tests, and (5) the third dicts test
'''

SPACING = '     '
TOL = 1e-6
TESTS = {'tuples': [], 'dicts': []}
 
tuples_func_table = {'sphere2cart': coordinates_tuples.sphere2cart,
                    'sphere2cyl': coordinates_tuples.sphere2cyl,
                    'cyl2sphere': coordinates_tuples.cyl2sphere,
                    'cyl2cart': coordinates_tuples.cyl2cart,
                    'cart2sphere': coordinates_tuples.cart2sphere,
                    'cart2cyl': coordinates_tuples.cart2cyl}

dicts_func_table = {'sphere2cart': coordinates_dicts.sphere2cart,
                   'sphere2cyl': coordinates_dicts.sphere2cyl,
                   'cyl2sphere': coordinates_dicts.cyl2sphere,
                   'cyl2cart': coordinates_dicts.cyl2cart,
                   'cart2sphere': coordinates_dicts.cart2sphere,
                   'cart2cyl': coordinates_dicts.cart2cyl}

def run_tuples_test(i, name, input, output):
  print '\nrunning tuples test %d...' % i

  result = tuples_func_table[name](input)
  for i, elmt in enumerate(result):
    if abs(elmt - output[i]) / abs(output[i]) > TOL:
      print '%s FAILED (expected: %s, actual: %s)' % (SPACING, str(output),
                                                      str(result))
      return False
  
  print '%s SUCCESS' % SPACING
  return True

def run_dicts_test(i, name, input, output):
  print '\nrunning dicts test %d...' % i

  result = dicts_func_table[name](input)
  for key in output:
    if key not in result:
      print '%s FAILED (missing key: %s)' % (SPACING, key)
      return False
    
    if abs(result[key] - output[key]) / abs(output[key]) > TOL:
      print '%s FAILED on %s (expected: %s, actual: %s)' % (SPACING,
                                                            str(key),
                                                            str(output[key]),
                                                            str(result[key]))
      print '%s input was: %s' % (SPACING, str(input))
      return False
  
  print '%s SUCCESS' % SPACING
  return True

def create_test(i, name, input, output, type):
  TESTS[type].append({'i': i, 'name': name, 'input': input, 'output': output})

create_test(1, 'cart2cyl',
            (1.0, 2.0, 3.0),
            (2.236067977499790, 1.107148717794090, 3.000000000000000),
            'tuples')

create_test(2, 'cyl2cart',
            (2.236067977499790, 1.107148717794090, 3.000000000000000),
            (1.0, 2.0, 3.0),
            'tuples')

create_test(3, 'cart2sphere',
            (1.0, 2.0, -3.0),
            (3.741657386773941, -0.930274014115472, 1.107148717794090),
            'tuples')

create_test(1, 'cart2sphere',
            {'x': 1.0, 'y': 2.0, 'z': -3.0},
            {'rho': 3.741657386773941, 'theta': -0.930274014115472,
            'phi': 1.107148717794090},
            'dicts')

def main():
  test_type = None
  if len(sys.argv) > 1:
    test_type = sys.argv[1]
    if test_type not in ['tuples', 'dicts']:
      print "UNKNOWN testing type: %s.  Use 'tuples' or 'dicts'." % test_type
      return

  test_number = None
  if len(sys.argv) > 2:
    test_number = int(sys.argv[2])
    if not 0 < test_number <= len(TESTS[test_type]):
      print 'invalid test number: ' + sys.argv[2]
      return

  test_funcs = {'tuples': run_tuples_test, 'dicts': run_dicts_test}

  if test_number is not None:
    test_funcs[test_type](**TESTS[test_type][test_number - 1])
  elif test_type is not None:
    for test in TESTS[test_type]:
      test_funcs[test_type](**test)
  else:
    for test in TESTS['tuples']:
      run_tuples_test(**test)
    for test in TESTS['dicts']:
      run_dicts_test(**test)


if __name__ == "__main__":
  main()
