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
    response = requests.get(url, headers=headers)
    print(token)

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
def get_latest_lang(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    print(token)

    if response.status_code == 200:
        events = response.json()
        filtered_events = []

        for event in events:
            event_type = event['type']
            if event_type in ['PushEvent', 'CreateEvent', 'PullRequestEvent']:
                filtered_events.append(event)

        if filtered_events:
            
            lang_1 , lang_2 , lang_3 = get_repository_language(filtered_events[0]['repo']['name'] ) , get_repository_language(filtered_events[1]['repo']['name']) , get_repository_language(filtered_events[2]['repo']['name'])
            unique_languages = set(lang for lang in [lang_1, lang_2, lang_3] if lang is not None)
            non_identical_languages = [lang for lang in unique_languages if list(unique_languages).count(lang) == 1]

            return non_identical_languages 

        else:
            return "No relevant activities found for this user."
    else:
        return f"Error fetching activities: {response.status_code}"

#-------------------------------------------------------------
def get_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    response = requests.get(url)
    if response.status_code == 200:
        return [{'login': contributor['login']} for contributor in response.json()]
    else:
        print(f"Error fetching contributors for {repo}: {response.status_code}")
        return []

def get_user_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[:10] 
    else:
        print(f"Error fetching events for {username}: {response.status_code}")
        return []

def get_user_contributors(username):
    events = get_user_events(username)
    contributors_set = set() 

    for event in events:
        repo = event['repo']['name']
        contributors = get_contributors(repo)
        for contributor in contributors:
            contributors_set.add(contributor['login'])

    contributors_list = list(contributors_set)  
    
    
    username_lower = username.lower()
    print(username_lower)
    contributors_list = [contributor for contributor in contributors_list if contributor != username_lower]
    print(contributors_list)
    return contributors_list  

#-------------------------------------------------------------
def get_repository_language(repo_name):
    url = f"https://api.github.com/repos/{repo_name}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        language = repo_info.get('language', 'No language specified')

        if language is not None:
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
username = "Seyedsahel"
# repo_languages = get_repo_languages(username)
# print(repo_languages)

# language_count = count_repos_by_language(repo_languages)
# print(language_count)

# latest_activity = get_latest_activity(username)
# print(latest_activity)
# print("------------------------------------------")
print(get_latest_lang(username))
print("------------------------------------------")

contributors_list = get_user_contributors(username)
print(contributors_list)

#-------------------------------------------------------------
