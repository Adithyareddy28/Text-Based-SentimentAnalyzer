from django.test import TestCase
from .utils import classify_sentiment

class SentimentAnalysisTest(TestCase):
    def test_sentiment_classification(self):
        result = classify_sentiment("I love programming")
        self.assertIn(result, ['positive', 'negative', 'neutral'])
