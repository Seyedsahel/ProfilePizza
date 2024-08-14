import requests

def get_repo_names(username):
    url = f"https://api.github.com/users/{username}/repos"
    print(url)

    
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        repos = response.json()
        
        repo_names = [repo['name'] for repo in repos]
        
        return repo_names
    else:
        print(f"Error: {response.status_code}")
        return []


username = "tahamusvi"
repo_names = get_repo_names(username)

print(repo_names)
