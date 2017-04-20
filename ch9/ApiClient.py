from collections import Counter

import requests, json
from dateutil.parser import parse

serialized = """{   "title" : "Data Science Book",
                    "author" : "Joel Grus",
                    "publicationYear" : 2014,
                    "topics" : ["data", "science", "data science"] }"""

# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print deserialized

endpoint = "https://api.github.com/users/Ludden/repos"

repos = json.loads(requests.get(endpoint).text)

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
print month_counts
print weekday_counts

last_5_repos = sorted(repos,
                      key=lambda r: r["created_at"],
                      reverse=True)[:5]
last_5_languages = sorted(repo["language"] for repo in last_5_repos)

print last_5_languages
