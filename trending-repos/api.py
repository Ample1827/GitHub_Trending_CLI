import requests
import sys

def fetch_repos(start_date_str, limit):
    
    base_url ="https://api.github.com/search/repositories"
    query_params = {
        "q": ("created:>" + start_date_str),
        "sort": "stars",
        "order":"desc",
        "per_page": 100,
    }
    
    response = requests.get(base_url, params=query_params)
    
    data = response.json()
    # print (response.status_code)
    return data ["items"]
    