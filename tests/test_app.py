
import unittest

from app import app


class TestFlaskApplication(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Sentiment Analysis", response.data)

    def test_positive_json_analysis(self):
        response = self.client.post(
            "/analyze",
            json={"text": "I absolutely love this product!"}
        )

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["sentiment"], "Positive")
        self.assertGreater(data["polarity"], 0)

    def test_negative_json_analysis(self):
        response = self.client.post(
            "/analyze",
            json={"text": "This product is terrible and disappointing."}
        )

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["sentiment"], "Negative")
        self.assertLess(data["polarity"], 0)

    def test_neutral_json_analysis(self):
        response = self.client.post(
            "/analyze",
            json={"text": "The meeting starts at 10 AM."}
        )

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["sentiment"], "Neutral")
        self.assertEqual(data["polarity"], 0.0)

    def test_empty_json_input(self):
        response = self.client.post(
            "/analyze",
            json={"text": "   "}
        )

        self.assertEqual(response.status_code, 400)

    def test_missing_json_text(self):
        response = self.client.post(
            "/analyze",
            json={}
        )

        self.assertEqual(response.status_code, 400)

    def test_text_exceeds_limit(self):
        response = self.client.post(
            "/analyze",
            json={"text": "a" * 5001}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "5,000 characters",
            response.get_json()["error"]
        )

    def test_text_at_limit(self):
        response = self.client.post(
            "/analyze",
            json={"text": "a" * 5000}
        )

        self.assertEqual(response.status_code, 200)

    def test_html_form_submission(self):
        response = self.client.post(
            "/analyze",
            data={"text": "I absolutely love this product!"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Positive", response.data)
        self.assertIn(b"Polarity", response.data)
        self.assertIn(b"Subjectivity", response.data)

    def test_empty_html_form(self):
        response = self.client.post(
            "/analyze",
            data={"text": "   "}
        )

        self.assertEqual(response.status_code, 400)

    def test_long_html_form(self):
        response = self.client.post(
            "/analyze",
            data={"text": "a" * 5001}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"5,000 characters", response.data)

    def test_unsupported_content_type(self):
        response = self.client.post(
            "/analyze",
            data="plain text",
            content_type="text/plain"
        )

        self.assertEqual(response.status_code, 415)


if __name__ == "__main__":
    unittest.main()
