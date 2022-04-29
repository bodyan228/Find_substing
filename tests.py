from Algorithms.bmh import BMH
from Algorithms.kmp import KMP
from Algorithms.brute_force import Brute_Force
from Algorithms.rabin_karp import RabinCarp
import unittest


class TestSubstring(unittest.TestCase):

    with open("input.txt") as file:
        original = file.read()

    def test_rabin_karp(self):
        self.assertEqual(RabinCarp("test from test", "e").testing(), (1, 2))
        self.assertEqual(RabinCarp("test from test", "fq").testing(),
                         (-1, 0))
        self.assertEqual(RabinCarp(self.original, "k").testing(),
                         (7223, 72))
        self.assertEqual(RabinCarp("вроврпгшвпшвгшшкп", "в").testing(), (0, 4))

    def test_brute_force(self):
        self.assertEqual(Brute_Force("test from test", "t").testing(),
                         (0, 3))
        self.assertEqual(Brute_Force("test from test", "a").testing(),
                         (-1, 0))
        self.assertEqual(Brute_Force("что-то на нерусском", "-").testing(),
                         (3, 1))
        self.assertEqual(Brute_Force(self.original, "k").testing(),
                         (7223, 72))

    def test_kmp(self):
        self.assertEqual(KMP("Privet, mead dft vanya", "a").testing(),
                         (10, 3))
        self.assertEqual(KMP("Privet, some_text vanya", "]").testing(),
                         (-1, 0))
        self.assertEqual(KMP("Privet, some_text vanya", "P").testing(), (0, 1))
        self.assertEqual(KMP(self.original, "k").testing(), (7223, 72))

    def test_bmh(self):
        self.assertEqual(BMH("something here ma write", "a").testing(),
                         (16, 1))
        self.assertEqual(BMH("something here ma write", "k").testing(),
                         (-1, 0))
        self.assertEqual(BMH("Небольшой текстнаписаннарусском", "с").testing(),
                         (13, 4))
        self.assertEqual(BMH(self.original, "k").testing(),
                         (7223, 72))
