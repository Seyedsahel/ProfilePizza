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
            latest_event = filtered_events[0]  # جدیدترین فعالیت
            return latest_event['repo']['name']
        else:
            return "No relevant activities found for this user."
    else:
        return f"Error fetching activities: {response.status_code}"

# مثال استفاده

username = "tahamusvi"
latest_activity = get_latest_activity(username, token)
print(latest_activity)
