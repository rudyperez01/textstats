import unittest

from textstats import count_lines, count_words, count_chars


class TextStatsTests(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words(""), 0)

    def test_count_lines(self):
        self.assertEqual(count_lines("one\ntwo\nthree"), 3)
        self.assertEqual(count_lines(""), 0)


if __name__ == "__main__":
    unittest.main()
