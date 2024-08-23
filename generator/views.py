from django.http import HttpResponse
from .models import Record
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from main import *

def svg_generator(request,username):
    try:
        record = Record.objects.get(username=username)
        record.inc_count()

    except Record.DoesNotExist:
        record = Record(username=username)

    record.save()


    #----------------------------------------
    bgcolor = request.GET.get('bgcolor', 'f4f4f4')
    text_color = request.GET.get('textcolor', get_complementary_color(bgcolor))
    no_bg = request.GET.get('no_bg', 'false').lower() == 'true'

    # Get user-defined width and height or use default values
    width = int(request.GET.get('width', 600))
    height = int(request.GET.get('height', 400))

    # Determine font size based on SVG dimensions if not provided
    font_size = int(request.GET.get('font_size', min(height // 15, width // 20)))  # Adjust based on both dimensions

    line_height = font_size * 1.5  # Space between lines
    max_width = width - 40  # Maximum width for text (considering padding)

    #----------------------------------------
    # section offline
    # latest_activity = {'type': 'PushEvent',
    #  'repo_name': 'Seyedsahel/ProfilePizza',
    #   'repo_url': 'https://api.github.com/repos/Seyedsahel/ProfilePizza',
    #    'repo_lang': 'Python'}  

    # co_name , working_on = latest_activity['repo_name'].split('/')
    # working_on_with_link = f'<a href="https://github.com/{latest_activity["repo_name"]}">{working_on}</a>'
    

    # repo_languages = {'Captcha-breaker': 'Python', 'Data-Structure-Coursera': 'C#', 'Emergency-pm': 'CSS', 'friendZone': 'Jupyter Notebook', 'images': 'Jupyter Notebook', 'MalwareDetector': 'Python', 'Petro-Lithology-Prediction': 'Jupyter Notebook', 'quera-solutions': 'Python', 'Stratego': 'Java', 'Sudoku_cpp': 'C++', 'Toos': 'Python', 'webShop': 'Python', 'Web_Security_tools': 'Python', 'words': 'Python', 'xv6-public': 'C'}

    # language_count = list(count_repos_by_language(repo_languages))

    # co_names = ['Sahel',
    #     'Reza',
    #     'Omid',
    #     ]
    #----------------------------------------
    # 0
    response_events = get_user_events(username)

    # 1
    latest_activity = get_latest_activity(response_events)
    # print(latest_activity)

    # 2
    co_name , working_on = latest_activity['repo_name'].split('/')
    working_on_with_link = f'<a href="https://github.com/{latest_activity["repo_name"]}">{working_on}</a>'
    
    # 3
    repo_languages = get_repo_languages(username)
    # print(repo_languages)

    language_count = list(count_repos_by_language(repo_languages))
    # print(language_count)

    # 4
    co_names = get_user_contributors(username,response_events)
    #----------------------------------------
    texts = [
        f"🚀 Right now, I'm diving into {latest_activity['repo_lang']}.",
        f'🔧 I’m currently working on my {working_on} project.',
        f"📚  Ask me about {language_count[0]} and {language_count[1]}",
        f"{adieu(co_names)}",
    ]

    # Calculate the height of the background box
    total_height = 20  # Initial padding
    wrapped_texts = []

    # Wrap the texts
    for text in texts:
        wrapped_lines = wrap_text(text, max_width, font_size)
        wrapped_texts.extend(wrapped_lines)
        total_height += len(wrapped_lines) * line_height

    # Ensure total height doesn't exceed user-defined height
    total_height = min(total_height, height)

    # Set a top margin for the text
    margin = 20 * total_height // 100  # Adjust this value as needed

    svg_content = f'''
    <svg width="{width}" height="{total_height + margin // 2}" xmlns="http://www.w3.org/2000/svg">
        <style>
            .text {{ font-family: Arial, sans-serif; font-size: {font_size}px; fill: #{text_color}; }}
        </style>
        {'<rect width="100%" height="100%" fill="#' + bgcolor + '" rx="10" ry="10"/>' if not no_bg else ''}
    '''

    # Add wrapped texts to the SVG with top margin
    for i, line in enumerate(wrapped_texts):
        svg_content += f'<text x="20" y="{margin + line_height * i}" class="text">{line}</text>\n'

    svg_content += '</svg>'

    svg_content = svg_content.replace(working_on,working_on_with_link)
    for x in co_names:
        
        svg_content = svg_content.replace(x,f'<a href="https://github.com/{x}">{x}</a>')

    # print(svg_content)
    return HttpResponse(svg_content, content_type='image/svg+xml')
