from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SearchHistory
from .serializers import WordFrequencySerializer, SearchHistorySerializer, GetSearchHistorySerializer
import requests
from bs4 import BeautifulSoup
from collections import Counter
from django.http import JsonResponse
import time
import datetime

@api_view(['GET'])
def word_frequency_analysis(request):

    # Validate payload
    serializer = WordFrequencySerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    topic = serializer.validated_data['topic']
    numOfCommonWords = serializer.validated_data['numOfCommonWords']
    
    # Fetch Wikipedia article
    url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return Response({'detail': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

    # Parse the article content
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join(paragraph.get_text() for paragraph in paragraphs)
    
    # Process text for word frequency
    words = text.split()
    word_count = Counter(words)
    most_common_words = word_count.most_common(numOfCommonWords)
    
    # Save to search history
    search_history = SearchHistory(topic=topic, topWords=dict(most_common_words), createdAt=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    search_history.save()
    
    return Response({'topic': topic, 'topWords': most_common_words})

   

@api_view(['GET'])
def get_search_history(request):

    # Validate payload
    serializer = GetSearchHistorySerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Set up pagination
    page_number = serializer.validated_data['page']
    limit = 10
    offset = (page_number - 1) * limit
    totalHistoryCount = SearchHistory.objects.count()

    # fetch all history ordered by descending createdAt with limit and offset
    history = SearchHistory.objects.all().order_by('-createdAt')[offset:offset+limit]

    # serialize data for sending response
    serializer = SearchHistorySerializer(history, many=True)

    data = {
        'page': page_number,
        'total_pages': totalHistoryCount//limit,
        'results': serializer.data
    }

    return JsonResponse(data)

