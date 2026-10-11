import unittest

from src.sentiment import analyze_sentiment


class TestSentimentAnalysis(unittest.TestCase):

    def test_positive_sentiment(self):
        result = analyze_sentiment(
            "I absolutely love this product!"
        )

        self.assertEqual(result["sentiment"], "Positive")
        self.assertGreater(result["polarity"], 0)

    def test_negative_sentiment(self):
        result = analyze_sentiment(
            "This product is terrible and disappointing."
        )

        self.assertEqual(result["sentiment"], "Negative")
        self.assertLess(result["polarity"], 0)

    def test_neutral_sentiment(self):
        result = analyze_sentiment(
            "The meeting starts at 10 AM."
        )

        self.assertEqual(result["sentiment"], "Neutral")
        self.assertEqual(result["polarity"], 0.0)

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            analyze_sentiment("")

    def test_whitespace_text(self):
        with self.assertRaises(ValueError):
            analyze_sentiment("   ")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            analyze_sentiment(None)

    def test_result_structure(self):
        result = analyze_sentiment("I love Python!")

        self.assertEqual(
            set(result.keys()),
            {"sentiment", "polarity", "subjectivity"}
        )

        self.assertIsInstance(result["polarity"], float)
        self.assertIsInstance(result["subjectivity"], float)


if __name__ == "__main__":
    unittest.main()
