import click
from datetime import datetime, timedelta, date
from api import fetch_repos
from display import display_repos

@click.command()

@click.option(
    "--duration", 
    type=click.Choice(['year', 'month', 'week', 'today'], case_sensitive=False), 
    default="today", 
    help="Define the time frame" 
)

@click.option(
    "--limit", 
    type=int, 
    default=10, 
    help="The maximum number of items."
)

def main(duration, limit):
    click.echo(f"Date successfully set to: {duration}")
    click.echo(f"Limit successfully set to: {limit}")
    
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
    print(start_date_str)

    repos = fetch_repos(start_date_str, limit)
    
    display_repos(repos, duration)
    
if __name__ == "__main__":
    main()
