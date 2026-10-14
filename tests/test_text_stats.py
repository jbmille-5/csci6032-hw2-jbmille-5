import unittest

from src.text_stats import calculate_stats


class CalculateStatsTests(unittest.TestCase):
    def test_counts_lines_words_and_characters(self):
        text = "Hello, world!\nSecond line."

        self.assertEqual(
            calculate_stats(text),
            {"lines": 2, "words": 4, "characters": 26},
        )

    def test_empty_text_has_no_content(self):
        self.assertEqual(
            calculate_stats(""),
            {"lines": 0, "words": 0, "characters": 0},
        )

    def test_unicode_characters_are_counted(self):
        self.assertEqual(
            calculate_stats("café\n"),
            {"lines": 1, "words": 1, "characters": 5},
        )


if __name__ == "__main__":
    unittest.main()
