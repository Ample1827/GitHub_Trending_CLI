import pyfiglet

def display_repos(repos, duration):
    banner = pyfiglet.figlet_format("TRENDING GITHUB REPOS", font="digital")
    print(banner)
    
    for repo in repos:
        
        print (repo["name"])
        print (repo["stargazers_count"])
        print (repo["language"])
        print (repo["description"])
        print (repo["html_url"])
            