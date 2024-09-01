# 0
    # response_events = get_user_events(username)

    # # 1
    # latest_activity = get_latest_activity(response_events,username)
    

    # # 2
    # co_name , working_on = latest_activity['repo_name'].split('/')
    # working_on_with_link = f'<a href="https://github.com/{latest_activity["repo_name"]}">{working_on}</a>'
    
    # # 3
    # repo_languages = get_repo_languages(username)
    

    # language_count = list(count_repos_by_language(repo_languages))
    

    # # 4
    # co_names = get_user_contributors(username,response_events)
    
    # # 5
    # last_star = get_user_satr(response_events)
    # last_star_repo_name = last_star.split('/')[1]
    # last_star_with_link = f'<a href="https://github.com/{last_star}">{last_star_repo_name}</a>'
    #----------------------------------------