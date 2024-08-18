import requests
# main.py
from config.settings import TOKEN
token = TOKEN
#-------------------------------------------------------------
def get_repo_languages(username):
    print(token)
    repos_url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(repos_url,headers = headers, timeout=1000)
    print("d")
    
    if response.status_code == 200:
        repos = response.json()
        
        repo_languages = {}
        
        for repo in repos:
            repo_name = repo['name']
            language = repo.get('language', 'No language specified')
            if language == None :
                continue
            repo_languages[repo_name] = language
        
        return repo_languages
    else:
        print(f"Error: {response.status_code}")
        return {}
#-------------------------------------------------------------    
def count_repos_by_language(repo_languages):
    language_count = {}
    
    for language in repo_languages.values():
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
            
    language_count = dict(sorted(language_count.items(), key=lambda item: item[1], reverse=True))
            
    return language_count
#-------------------------------------------------------------
def get_latest_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Authorization': f'token {token}'}
    # response = requests.get(url, headers=headers)
    # print(token)

    if response.status_code == 200:
        events = response.json()
        filtered_events = []

        for event in events:
            event_type = event['type']
            if event_type in ['PushEvent', 'CreateEvent', 'PullRequestEvent']:
                filtered_events.append(event)

        if filtered_events:
            latest_event={}
            latest_event['type'] = filtered_events[0]['type'] 
            latest_event['repo_name'] = filtered_events[0]['repo']['name'] 
            latest_event['repo_url'] = filtered_events[0]['repo']['url'] 
            latest_event['repo_lang'] = get_repository_language(latest_event['repo_name'])
            return latest_event
        else:
            return "No relevant activities found for this user."
    else:
        return f"Error fetching activities: {response.status_code}"
#-------------------------------------------------------------
def get_repository_language(repo_name):
    url = f"https://api.github.com/repos/{repo_name}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        language = repo_info.get('language', 'No language specified')
        return language
    else:
        return f"Error fetching repository info: {response.status_code}"
#-------------------------------------------------------------
def generate_markdown(repo_languages, language_count, latest_activity):
    markdown = "# My GitHub Stats\n\n"
    
    markdown += "## Repository Languages\n"
    for repo, language in repo_languages.items():
        markdown += f"- **{repo}**: {language}\n"
    
    markdown += "\n## Language Count\n"
    for language, count in language_count.items():
        markdown += f"- **{language}**: {count} repositories\n"
    
    markdown += "\n## Latest Activity\n"

    if isinstance(latest_activity, dict):
            markdown += f"- **Type**: {latest_activity['type']}\n"
            markdown += f"- **Repository**: [{latest_activity['repo_name']}]({latest_activity['repo_url']})\n"
            markdown += f"- **Language**: {latest_activity['repo_lang']}\n"
    else:
        markdown += latest_activity

    return markdown
#-------------------------------------------------------------
# username = "omidTarabavar"
# token = TOKEN
# repo_languages = get_repo_languages(username,token)
# print(repo_languages)

# language_count = count_repos_by_language(repo_languages)
# print(language_count)

# latest_activity = get_latest_activity(username, token)
# print(latest_activity)
#-------------------------------------------------------------