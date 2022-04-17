from SearchSubstrings import search_substrings
import unittest


class TestSubstring(unittest.TestCase):

    search = search_substrings()

    def setUp(self):
        self.r_k = self.search.RabbinKarp
        self.b_f = self.search.BruthForce
        self.k_m_p = self.search.KMP
        self.b_m_h = self.search.BMH

    def test_Rabin_Karp(self):
        self.assertEqual(self.r_k("test from test", "f"), 5)

    def test_Bruth_Force(self):
        self.assertEqual(self.b_f("test from test", "t"), 0)

    def test_KMP(self):
        self.assertEqual(self.k_m_p("Privet, menya zovyt vanya", "a"), 12)
        self.assertEqual(self.k_m_p("Privet, menya zovyt vanya", "]"), -1)

    def test_BMH(self):
        self.assertEqual(self.b_m_h("something here may write,"
                                    " i don't understand", "a"), 2)
