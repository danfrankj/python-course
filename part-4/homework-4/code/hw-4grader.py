#hw-4grader.py
import random
import unittest
import sys
import re
import inspect
import numpy as np

def my_kde(x, bw, data):
    # bad kde so as not to give away the answer
    total = 0
    size = 0
    for d in data:
        size += 1
        val = 1. - abs(x - d) / float(bw)
        if val < 0:
            val = 0
        val /= bw
        total += val
    return total / size

def grade(path):
    sys.path.append(path)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHw4)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    PF = result.wasSuccessful()
    errororfails = len(result.errors) + len(result.failures)
    PF = "PASS" if errororfails == 0 else "FAIL"
    score = 100 if PF == "PASS" else 0
    return score, PF


class TestHw4(unittest.TestCase):

    def get_lines(self, func):
        lines = inspect.getsourcelines(func)[0]
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if (line.find('#') != 0 and
                                            line.find('def') != 0 and
                                            line.find('"""') != 0)]
        return lines

    def search_lines(self, pattern, lines):
        for line in lines:
            if re.search(pattern, line) is not None:
                return True
        return False

    def setUp(self):
        N = 50
        self.expected = np.power(2., np.arange(N))
        return None

    def test_prof_main(self):
        import prof
        print "\n"
        prof.main()
        print "\n"

    def test_empty_list(self):
        import prof
        lines = self.get_lines(prof.empty_list)

        self.assertTrue(
            self.search_lines(".* *= *\[ *\]|.+ *= *list\(*\)", lines),
            "please initialize an empty list first")

        self.assertTrue(
            self.search_lines("for +[A-Za-z_0-9]+ +in +", lines),
            "please use a for loop")

        out = np.array(prof.empty_list())
        self.assertTrue(np.linalg.norm(out - self.expected) < 1e-6,
                        'output of function is not expected 50 powers of two')

    def test_preallocated_list(self):
        import prof
        lines = self.get_lines(prof.preallocated_list)

        self.assertTrue(
            self.search_lines("for +[A-Za-z_0-9]+ +in +", lines),
            "please use a for loop")
        self.assertTrue(
            self.search_lines("[A-Za-z_0-9]+\[[A-Za-z_0-9]+\] *= *", lines),
            "assign to list sequentially")

        out = np.array(prof.preallocated_list())
        self.assertTrue(np.linalg.norm(out - self.expected) < 1e-6,
                        'output of function is not expected 50 powers of two')

    def test_lst_comp(self):
        import prof
        lines = self.get_lines(prof.lst_comp)

        self.assertTrue(len(lines) == 1,
                        "please create and return the list" +
                        "compreshension in one line")

        pat = "return +\[.* +for +[A-Za-z_0-9]+ +in +.*\]"
        self.assertTrue(
            self.search_lines(pat, lines),
            "please use a list comprehension and do not" +
            "use numpy i.e. use ** for power")

        out = np.array(prof.preallocated_list())
        self.assertTrue(np.linalg.norm(out - self.expected) < 1e-6,
                        'output of function is not expected 50 powers of two')

    def test_map_twos(self):
        import prof
        lines = self.get_lines(prof.map_twos)

        self.assertTrue(len(lines) == 1,
                        "please call and return the map function one line")

        pat = "return +map\(.*\)"
        self.assertTrue(
            self.search_lines(pat, lines),
            "please use the python map function")

        out = np.array(prof.map_twos())
        self.assertTrue(np.linalg.norm(out - self.expected) < 1e-6,
                        'output of function is not expected 50 powers of two')

    def test_twos_numpy(self):
        import prof
        lines = self.get_lines(prof.twos_numpy)

        self.assertTrue(len(lines) == 1,
                        "please create and return the map function one line")

        pat = "return +(np|numpy)\.power\(.*\)"
        self.assertTrue(
            self.search_lines(pat, lines),
            "please use numpy to compute the powers")

        out = np.array(prof.twos_numpy())
        self.assertTrue(np.linalg.norm(out - self.expected) < 1e-6,
                        'output of function is not expected 50 powers of two')

    def test_test_opt(self):
        import scipy_opt
        xstar = np.array([1., 0.])
        self.assertTrue(np.linalg.norm(xstar - scipy_opt.test_opt()) < 1e-4,
                        "answer does not satisfy Ax=b")

    def test_kde(self):
        import kde
        lines = inspect.getsourcelines(kde.kde)[0]
        lines = [line.strip() for line in lines]
        data = np.random.normal(size=100)
        bw = np.random.normal(1) + 10.
        query = np.random.normal(1)
        myout = my_kde(x=query, bw=bw, data=data)
        self.assertTrue(np.abs(kde.kde(x=query, bw=bw, data=data) - myout) < 1e-6,
                               'kde function does not return correct value')

        self.assertTrue(len(lines) == 1,
                        "please write your kde on one line, yes a def():" +
                        "counts so you cannot do that")

        pat = ".* +for +.*"
        self.assertFalse(
            self.search_lines(pat, lines),
            "please do not use the keyword for")

        pat = ".* +if +.*"
        self.assertFalse(
            self.search_lines(pat, lines),
            "please do not use the keyword if")

        pat = ".* +in +.*"
        self.assertFalse(
            self.search_lines(pat, lines),
            "please do not use the keyword in")

        pat = ".*vectorize.*"
        self.assertFalse(
            self.search_lines(pat, lines),
            "please do not use vectorize")

        pat = ".*map.*"
        self.assertFalse(
            self.search_lines(pat, lines),
            "please do not use map")





    def tearDown(self):
        return None
