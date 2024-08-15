from django.db import models

class SearchHistory(models.Model):

    # Model for the search_history table
    topic = models.CharField(max_length=255)
    topWords = models.JSONField()
    createdAt = models.DateTimeField()

    def __str__(self):
        return f"{self.topic}: {self.topWords}"
    
