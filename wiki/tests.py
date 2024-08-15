from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SearchHistory

class WordFrequencyTests(APITestCase):
    def test_word_frequency_analysis(self):
        url = reverse('word_frequency_analysis')
        data = {'topic': 'Python_(programming_language)', 'n': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('topic', response.data)
        self.assertIn('top_words', response.data)
        self.assertTrue(len(response.data['top_words']) <= 5)

    def test_search_history(self):
        # Add an entry to the history
        SearchHistory.objects.create(topic='Python_(programming_language)', top_words={'Python': 100, 'language': 50})
        url = reverse('search_history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertIn('topic', response.data[0])
        self.assertIn('top_words', response.data[0])
