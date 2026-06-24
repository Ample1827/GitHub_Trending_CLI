from rich.console import Console
from rich.table import Table

def display_repos(repos, duration):
    
    table = Table(title="Trending GitHub Repos", show_lines=True,)
    table.add_column("#")
    table.add_column("Name")
    table.add_column("Stars", justify="center")
    table.add_column("Coding Language", justify="center")
    table.add_column("Description")
    table.add_column("URL")
    
    console = Console()
    
    for index, repo in enumerate(repos, start=1):
        
        table.add_row(str(index), repo["name"], str(repo["stargazers_count"]) + " ⭐ ", repo["language"] or "Unknown", repo["description"] or "No description", repo["html_url"])
        
    console.print(table)
        