<h1>Django WIKI Project</h1>

Follow these steps to set up the server

<li>RUN pip3 install --no-cache-dir -r requirements.txt</li>
<li>RUN python3 manage.py migrate</li>
<li>RUN python3 manage.py runserver</li>

The server wil run at port 8000

<h2>API Endpoints</h2>

<h3>Word Frequency Endpoint</h3>

```
Endpoint: /wiki/word_frequency/
Method: GET
Request Body:
{
  "topic": "Bruce Lee",
  "numOfCommonWords": 3
}

Response:
{
    "topic": "Bruce Lee",
    "topWords": [
        [
            "the",
            420
        ],
        [
            "and",
            289
        ],
        [
            "to",
            272
        ]
    ]
}
```
<h3>Search History Endpoint</h3>

```
Endpoint: /wiki/search_history/
Method: GET
Request Body:
{
    "page":1
}

Response:
{
    "page": 1,
    "total_pages": 1,
    "results": [
        {
            "topic": "Bruce Lee",
            "topWords": {
                "the": 420,
                "and": 289,
                "to": 272
            }
        }
    ]
}
```
