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


def get_repo_languages(username):
    repos_url = f"https://api.github.com/users/{username}/repos"
    
    response = requests.get(repos_url)
    
    if response.status_code == 200:
        repos = response.json()
        
        repo_languages = {}
        
        for repo in repos:
            repo_name = repo['name']
            
            lang_url = repo['languages_url']
            lang_response = requests.get(lang_url)
            
            if lang_response.status_code == 200:
                languages = lang_response.json()
                main_language = max(languages, key=languages.get, default="Unknown")
                repo_languages[repo_name] = main_language
            else:
                repo_languages[repo_name] = "Error retrieving languages"
        
        return repo_languages
    else:
        print(f"Error: {response.status_code}")
        return {}

username = "tahamusvi"
repo_languages = get_repo_languages(username)
print(repo_languages)