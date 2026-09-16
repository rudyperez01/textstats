import unittest

from textstats import count_lines, count_words, count_chars, stats


class TextStatsTests(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words(""), 0)

    def test_count_lines(self):
        self.assertEqual(count_lines("one\ntwo\nthree"), 3)
        self.assertEqual(count_lines(""), 0)

    def test_count_chars(self):
        self.assertEqual(count_chars("hello"), 5)
        self.assertEqual(count_chars(""), 0)

    def test_stats(self):
        self.assertEqual(
            stats("one\ntwo three"),
            {"lines": 2, "words": 3, "chars": 13},
        )
        self.assertEqual(stats(""), {"lines": 0, "words": 0, "chars": 0})


if __name__ == "__main__":
    unittest.main()
