from rich.console import Console
from rich.table import Table

def display_repos(repos, duration):
    
    table = Table(title="Trending GitGub Repos", show_lines=True,)
    table.add_column("#")
    table.add_column("name")
    table.add_column("stargazers_count", justify="center")
    table.add_column("language", justify="center")
    table.add_column("description")
    table.add_column("html_url")
    
    console = Console()
    
    for index, repo in enumerate(repos, start=1):
        
        
        
        table.add_row(str(index), repo["name"], str(repo["stargazers_count"]) + " ⭐ ", repo["language"], repo["description"], repo["html_url"])
        
        
    console.print(table)
        