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
        self.assertEqual(RabinCarp("авыалоыашцтрулаатл", "а").testing(),
                         (0, 5))
        self.assertEqual(RabinCarp("12333332313344512", "6").testing(),
                         (-1, 0))
        self.assertEqual(RabinCarp("привет как дела", "ет").testing(),
                         (3, 1))
        self.assertEqual(RabinCarp("необычный случай", "н").testing(),
                         (0, 2))

    def test_brute_force(self):
        self.assertEqual(Brute_Force("test from test", "t").testing(),
                         (0, 3))
        self.assertEqual(Brute_Force("test from test", "a").testing(),
                         (-1, 0))
        self.assertEqual(Brute_Force("что-то на нерусском", "-").testing(),
                         (3, 1))
        self.assertEqual(Brute_Force(self.original, "k").testing(),
                         (7223, 72))
        self.assertEqual(Brute_Force("авыалоыашцтрулаатл", "о").testing(),
                         (5, 1))
        self.assertEqual(Brute_Force("12333332313344512", "6").testing(),
                         (-1, 0))
        self.assertEqual(Brute_Force("привет как дела", "привет").testing(),
                         (5, 1))
        self.assertEqual(Brute_Force("необычный случай", "нео").testing(),
                         (2, 1))
        self.assertEqual(Brute_Force(self.original, "k").testing(), (7223, 72))

    def test_kmp(self):
        self.assertEqual(KMP("Privet, mead dft vanya", "a").testing(),
                         (10, 3))
        self.assertEqual(KMP("Privet, some_text vanya", "]").testing(),
                         (-1, 0))
        self.assertEqual(KMP("необычный день", "ь").testing(), (13, 1))
        self.assertEqual(KMP("авыалоыашцтрулаатл", "о").testing(), (5, 1))
        self.assertEqual(KMP("12333332313344512", "6").testing(), (-1, 0))
        self.assertEqual(KMP("привет как дела", "привет").testing(), (5, 1))
        self.assertEqual(KMP("необычный случай", "нео").testing(), (2, 1))
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
        self.assertEqual(BMH("12333332313344512", "6").testing(), (-1, 0))
        self.assertEqual(BMH("привет как дела", "привет").testing(), (0, 1))
        self.assertEqual(BMH("необычный случай", "нео").testing(), (0, 1))
        self.assertEqual(BMH(self.original, "k").testing(), (7223, 72))
