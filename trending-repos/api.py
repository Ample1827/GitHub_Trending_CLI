import requests
import sys
from rich.console import Console
console = Console()

def fetch_repos(start_date_str, limit):
    
    try:
        
        base_url ="https://api.github.com/search/repositories"
        query_params = {
            "q": ("created:>" + start_date_str),
            "sort": "stars",
            "order":"desc",
            "per_page": 100,
        }
        
        response = requests.get(base_url, params=query_params)
        
        if response.status_code != 200:
            console.print (f"[red]GitHub returned an error — status code: {response.status_code} [/red]")
            sys.exit(1)
            
        data = response.json()
        
        return data ["items"][:limit]
    
    except requests.exceptions.ConnectionError:
        console.print ("[red]No internet connection![/red]")
        sys.exit(1)
        
    except requests.exceptions.Timeout:
        console.print ("[red]Timed out![/red]")
        sys.exit(1)
    
    except requests.exceptions.RequestException:
        console.print ("[red]general error[/red]")
        sys.exit(1)