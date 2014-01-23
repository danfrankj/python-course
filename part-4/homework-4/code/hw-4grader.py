#hw-4grader.py
import random
import unittest
import numpy as np
import sys
import re
import inspect


def grade(path):
    sys.path.append(path)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHw2)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    PF = result.wasSuccessful()
    total = result.testsRun
    errororfails = len(result.errors) + len(result.failures)
    PF = "PASS" if errororfails == 0 else "FAIL"
    score = 100 if PF == "PASS" else 0
    return score, PF

class TestHw4(unittest.TestCase):

    def get_lines(func):
        return inspect.getsourcelines(func)[0]

    def check_lines(lines):
        ".*"

    def setUp(self):
        return None

    def test_prof_main(self):
        import prof
        prof.main()

    def test_prof_empty_list():
        import prof
        lines = get_lines(prof.empty_list)
        pattern = " for .+ in "



    def test_ngram_onegram(self):
        import ngram
        cnts = ngram.ngram(n=1, k=1, document='test.txt')
        self.assertTrue(cnts.has_key("a"), 'ngram does not contain appropriate keys' + str(cnts))
        self.assertEqual(cnts["a"], 3, 'ngram count is incorrect' + str(cnts))
        self.assertEqual(len(cnts), 1, 'ngram should only contain top k counts' + str(cnts))



    def tearDown(self): 
        return None




