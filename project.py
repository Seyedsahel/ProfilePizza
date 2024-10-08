import requests
# main.py
from config.settings import TOKEN
token = TOKEN
#-------------------------------------------------------------

def get_user_events(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Authorization': f'token {token}'}
    response_events = requests.get(url, headers=headers)

    if response_events.status_code == 200:
        return response_events.json()
    else:
        print(f"Error fetching events for {username}: {response_events.status_code}")
        return []

#-------------------------------------------------------------
def get_filtered_events(events,filters):
    filtered_events = []

    for event in events:
        event_type = event['type']
        if event_type in filters:
            filtered_events.append(event)
    return filtered_events

#-------------------------------------------------------------
def adieu(names):
    num_names = len(names)
    if num_names == 0:
        return "I recently collaborated with NoOne :("
    if num_names == 1:
        return (f"I recently collaborated with {names[0]}.")
    elif num_names == 2:
        return (f"I recently collaborated with {names[0]} and {names[1]}.")
    else:
        output = "I recently collaborated with "
        for i in range(num_names):
            if i == num_names - 1:
                pass
            elif i == num_names - 2:
                output += f"{names[i]}, and {names[i+1]}."
            else:
                output += f"{names[i]}, "
        return (output)
#-------------------------------------------------------------
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')

    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
#-------------------------------------------------------------
def rgb_to_hex(rgb):
    return '{:02x}{:02x}{:02x}'.format(*rgb)
#-------------------------------------------------------------
def get_complementary_color(hex_color):
    rgb = hex_to_rgb(hex_color)
    comp_rgb = (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])
    return rgb_to_hex(comp_rgb)
#-------------------------------------------------------------
def wrap_text(text, max_width, font_size):
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        # Check if adding the next word exceeds the max width
        test_line = f"{current_line} {word}".strip()
        if len(test_line) * font_size / 2 > max_width:  # Approximate width calculation
            lines.append(current_line)
            current_line = word  # Start a new line
        else:
            current_line = test_line

    if current_line:  # Add the last line
        lines.append(current_line)

    return lines
#-------------------------------------------------------------
def get_repo_languages(username):
    # print(token)
    repos_url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(repos_url,headers = headers, timeout=1000)

    if response.status_code == 200:
        repos = response.json()
        
        repo_languages = {}
        
        for repo in repos:
            repo_name = repo['name']
            if repo_name == f"{username}" :
                continue
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
def get_latest_activity(response_events, username):
    filtered_events = get_filtered_events(response_events, ['PushEvent', 'CreateEvent', 'PullRequestEvent'])

    if filtered_events:
        for event in filtered_events:
            repo_name = event['repo']['name']
            if repo_name != username:
                latest_event = {}
                latest_event['type'] = event['type']
                latest_event['repo_name'] = repo_name
                latest_event['repo_url'] = event['repo']['url']
                latest_event['repo_lang'] = get_repository_language(repo_name)
                return latest_event

    return "No relevant activities found for this user."

    
#-------------------------------------------------------------
def get_latest_lang(response_events):
    filtered_events = get_filtered_events(response_events,['PushEvent', 'CreateEvent', 'PullRequestEvent'])

    if filtered_events:
        
        lang_1 , lang_2 , lang_3 = get_repository_language(filtered_events[0]['repo']['name'] ) , get_repository_language(filtered_events[1]['repo']['name']) , get_repository_language(filtered_events[2]['repo']['name'])
        unique_languages = set(lang for lang in [lang_1, lang_2, lang_3] if lang is not None)
        non_identical_languages = [lang for lang in unique_languages if list(unique_languages).count(lang) == 1]

        return non_identical_languages 

    else:
        return "No relevant activities found for this user."

#-------------------------------------------------------------
def get_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    response = requests.get(url)
    if response.status_code == 200:
        return [{'login': contributor['login']} for contributor in response.json()]
    else:
        print(f"Error fetching contributors for {repo}: {response.status_code}")
        return []
#-------------------------------------------------------------
def get_user_contributors(username,response_events):
    events = response_events[:10]
    events = get_filtered_events(events,['PushEvent', 'CreateEvent', 'PullRequestEvent'])

    contributors_set = set() 
    contributors = []
    for event in events:
        repo = event['repo']['name']
        if repo != f"{username}/{username}":
            contributors = get_contributors(repo)

        for contributor in contributors:
            contributors_set.add(contributor['login'])

    contributors_list = list(contributors_set)  
    username_lower = username.lower()
    
    contributors_list = [contributor for contributor in contributors_list if contributor.lower() != username_lower]
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
def get_user_satr(response_events):
    last_star = get_filtered_events(response_events,['WatchEvent'])
    return last_star[0]['repo']['name']
 
#-------------------------------------------------------------
def main():
        
    username = "seyedsahel"
    # response_events = get_user_events(username)

    # repo_languages = get_repo_languages(username)
    # print(repo_languages)

    # print(get_user_satr(response_events))

    # language_count = count_repos_by_language(repo_languages)
    # print(language_count)

    # latest_activity = get_latest_activity(response_events,username)
    # print(latest_activity)
    # print("------------------------------------------")
    # print(get_latest_lang(response_events))
    # print("------------------------------------------")

    # contributors_list = get_user_contributors(username,response_events)
    # print(contributors_list)

# -------------------------------------------------------------


if __name__ == "__main__":
    main()
