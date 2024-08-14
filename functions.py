import requests

def get_repo_names(username):
    url = f"https://api.github.com/users/{username}/repos"
    print(url)

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5',
    }       
    response = requests.get(url , headers = headers)
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
                # if main_language == "Unknown":
                #     continue
                repo_languages[repo_name] = main_language
            else:
                repo_languages[repo_name] = "Error retrieving languages"
        
        return repo_languages
    else:
        print(f"Error: {response.status_code}")
        return {}
    
def count_repos_by_language(repo_languages):
    language_count = {}
    
    for language in repo_languages.values():
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
            
    return language_count

username = "tahamusvi"
repo_languages = get_repo_languages(username)
print(repo_languages)

language_count = count_repos_by_language(repo_languages)
print(language_count)
