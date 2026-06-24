import click
from datetime import datetime, timedelta, date
from api import fetch_repos
from display import display_repos
from rich.console import Console
import questionary
import os 

@click.command()


def main():
    
    duration = questionary.select(
    "Choose duration:",
    choices=["today", "week", "month", "year"]
    ).ask()
    
    limit = int(questionary.text("How many repos to show?", default="10").ask())
    
    os.system('cls')
    
    today = datetime.now()
    
    if duration == ("today"):
        start_date  = today
    
    elif duration == ("week"):
        start_date  = today - timedelta(days=7)
        
    elif duration == ("month"):
        start_date = today - timedelta(days=30)
        
    elif duration == ("year"):
        start_date = today - timedelta(days=365)
        
    start_date_str = start_date.strftime("%Y-%m-%d")
    # print(start_date_str)

    console = Console()
    
    with console.status("Fetching trending repos..."):
        repos = fetch_repos(start_date_str, limit)
    
    display_repos(repos, duration)
    
    action = questionary.select(
    "What would you like to do?",
    choices=["Search again", "Exit"]
    ).ask()
    
    os.system('cls')
    
    if action == "Search again":
        return main()
    elif action == "Exit":
        console.print("Goodbye!")
    
if __name__ == "__main__":
    main()
