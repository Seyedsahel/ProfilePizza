import requests

def get_latest_activity(username, token):
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

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
            latest_event['repo_lang'] = get_repository_language(latest_event['repo_name'], token)
            return latest_event
        else:
            return "No relevant activities found for this user."
    else:
        return f"Error fetching activities: {response.status_code}"

def get_repository_language(repo_name, token):
    url = f"https://api.github.com/repos/{repo_name}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        language = repo_info.get('language', 'No language specified')
        return language
    else:
        return f"Error fetching repository info: {response.status_code}"


username = "tahamusvi"

latest_activity = get_latest_activity(username, token)
print(latest_activity)
