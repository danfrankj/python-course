import random
import unittest
import numpy as np
import sys


def grade(path):
    sys.path.append(path)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHw3)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    PF = result.wasSuccessful()
    total = result.testsRun
    errororfails = len(result.errors) + len(result.failures)
    PF = "PASS" if errororfails <= 1 else "FAIL"
    score = 50 if PF == "PASS" else 0
    return score, PF

class TestHw3(unittest.TestCase):

    def setUp(self):
        with open('test.txt', 'w') as f:
            f.write("a a a b b")
        with open('testvec1.txt','w') as g:
            g.write('1.1\n2.3')

    def test_ngram_onegram(self):
        import ngram
        cnts = ngram.ngram(n=1, k=1, document='test.txt')
        self.assertTrue(cnts.has_key("a"), 'ngram does not contain appropriate keys' + str(cnts))
        self.assertEqual(cnts["a"], 3, 'ngram count is incorrect' + str(cnts))
        self.assertEqual(len(cnts), 1, 'ngram should only contain top k counts' + str(cnts))

    def test_ngram_twogram(self):
        import ngram
        cnts = ngram.ngram(n=2, k=1, document='test.txt')
        self.assertTrue(cnts.has_key("a a"), 'ngram does not contain appropriate keys' + str(cnts))
        self.assertEqual(cnts["a a"], 2, 'ngram count is incorrect' + str(cnts))
        self.assertEqual(len(cnts), 1, 'ngram should only contain top k counts' + str(cnts))

    def test_portfolio(self):
        import stocks
        p = stocks.Portfolio()
        p.add_stock(symbol="A", price_per_share=1.5, shares=1)
        p.add_stock(symbol="B", price_per_share=2, shares = 1)
        self.assertEqual(p.most_money(), "B")

        self.assertTrue("A" in p)
        self.assertTrue("B" in p)

        p.add_stock(symbol="A", price_per_share=1.5, shares=9)
        self.assertEqual(p.most_money(), "A")

        p.add_stock(symbol="B", price_per_share=1., shares=9)
        self.assertEqual(p.most_money(), "A")


    def test_read_data(self):
        import myfirstnumpy
        lst = myfirstnumpy.read_data('testvec1.txt')
        self.assertEqual(lst, [1.1, 2.3])

    def test_elementwise_write(self):
        import myfirstnumpy
        a = [1.1, 2.3]
        b = [7.2, 8.2]
        myfirstnumpy.elementwise_write(a, b, 'outvec.txt')
        with open('outvec.txt', 'r') as f:
            outvec = [round(float(l.strip()), 6) for l in f]

        self.assertEqual(len(outvec), 2)
        self.assertAlmostEqual(outvec[0], a[0] * b[0])
        self.assertAlmostEqual(outvec[1], a[1] * b[1])	


    def test_norm_sub(self):
        import myfirstnumpy
        a = np.random.random(10)
        b = np.random.random(10)
        out = myfirstnumpy.norm_sub(a, b)
        self.assertEqual(np.linalg.norm(a - b, 1), out)


    def test_scale(self):
        import myfirstnumpy
        A = np.array([[2, 3], [4, 5], [8, 9]])
        A = myfirstnumpy.scale(A)
        desired = np.array([[20, 6], [4, 25], [16, 18]])
        self.assertTrue(np.all(A == desired))


    def tearDown(self): 
        return None


