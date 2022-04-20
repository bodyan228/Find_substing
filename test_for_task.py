from BMH import testingBMH
from KMP import testingKMP, find_prefix
from Brute_Force import testing_Brute_Force
from Rabin_Karp import testing_al_RabinKarp
import unittest


class TestSubstring(unittest.TestCase):

    def setUp(self):
        self.r_k = testing_al_RabinKarp
        self.b_f = testing_Brute_Force
        self.k_m_p = testingKMP
        self.b_m_h = testingBMH
        self.find_pr = find_prefix

    def test_Rabin_Karp(self):
        self.assertEqual(self.r_k("test from test", "f"), 5)
        self.assertEqual(self.r_k("test from test", "fq"), -1)

    def test_Brute_Force(self):
        self.assertEqual(self.b_f("test from test", "t"), 0)
        self.assertEqual(self.b_f("test from test", "a"), -1)

    def test_KMP(self):
        self.assertEqual(self.k_m_p("Privet, mead dft vanya", "a"), 10)
        self.assertEqual(self.k_m_p("Privet, some_text vanya", "]"), -1)
        self.assertEqual(self.find_pr("pattern"), [0, 0, 0, 0, 0, 0, 0])

    def test_BMH(self):
        self.assertEqual(self.b_m_h("something here may write,"
                                    " i don't understand", "a"), 16)
        self.assertEqual(self.b_m_h("something here may write,"
                                    " i don't understand", "["), -1)


if __name__ == '__main__':
    unittest.main()
