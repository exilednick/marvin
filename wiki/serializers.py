from rest_framework import serializers
from .models import SearchHistory

class WordFrequencySerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=255)
    numOfCommonWords = serializers.IntegerField()

class GetSearchHistorySerializer(serializers.Serializer):
    page = serializers.IntegerField()

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ['topic', 'topWords']
