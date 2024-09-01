from django.http import HttpResponse
from .models import Record
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from project import *
from .sample import sample,line_component
from .icon_svg import *
from  config.settings import deploy


def svg_generator(request,username):
    try:
        record = Record.objects.get(username=username)
        record.inc_count()

    except Record.DoesNotExist:
        record = Record(username=username)

    record.save()


    #----------------------------------------
    bgcolor = request.GET.get('bgcolor', '20232A')
    header_color =  request.GET.get('hcolor', 'DA5858')
    text_color = request.GET.get('textcolor', get_complementary_color(bgcolor))
    no_bg = request.GET.get('no_bg', 'false').lower() == 'true'

    # Get user-defined width and height or use default values
    width = int(request.GET.get('width', 505))
    height = int(request.GET.get('height', 195))

    # Determine font size based on SVG dimensions if not provided
    font_size = int(request.GET.get('font_size', min(height // 25, width // 30)))  # Adjust based on both dimensions

    line_height = font_size * 1.5  # Space between lines
    max_width = width - 100  # Maximum width for text (considering padding)

    #----------------------------------------
    # section offline
    if not deploy:
        latest_activity = {'type': 'PushEvent',
        'repo_name': 'Seyedsahel/ProfilePizza',
        'repo_url': 'https://api.github.com/repos/Seyedsahel/ProfilePizza',
        'repo_lang': 'Python'}  

        co_name , working_on = latest_activity['repo_name'].split('/')
        working_on_with_link = f'<a href="https://github.com/{latest_activity["repo_name"]}">{working_on}</a>'
        

        repo_languages = {'Captcha-breaker': 'Python', 'Data-Structure-Coursera': 'C#', 'Emergency-pm': 'CSS', 'friendZone': 'Jupyter Notebook', 'images': 'Jupyter Notebook', 'MalwareDetector': 'Python', 'Petro-Lithology-Prediction': 'Jupyter Notebook', 'quera-solutions': 'Python', 'Stratego': 'Java', 'Sudoku_cpp': 'C++', 'Toos': 'Python', 'webShop': 'Python', 'Web_Security_tools': 'Python', 'words': 'Python', 'xv6-public': 'C'}

        language_count = list(count_repos_by_language(repo_languages))

        co_names = ['Sahel',
            'Reza',
            'Omid',
            ]

        last_star = "omidTarabavar/ICPC_Fund"
        last_star_repo_name = last_star.split('/')[1]
        last_star_with_link = f'<a href="https://github.com/{last_star}">{last_star_repo_name}</a>'
    #----------------------------------------
    else:
        # 0
        response_events = get_user_events(username)

        # 1
        latest_activity = get_latest_activity(response_events,username)
        

        # 2
        co_name , working_on = latest_activity['repo_name'].split('/')
        working_on_with_link = f'<a href="https://github.com/{latest_activity["repo_name"]}" style="color: inherit; text-decoration: none;"  target="blank">{working_on}</a>'
        
        # 3
        repo_languages = get_repo_languages(username)
        

        language_count = list(count_repos_by_language(repo_languages))
        

        # 4
        co_names = get_user_contributors(username,response_events)
        
        # 5
        last_star = get_user_satr(response_events)
        last_star_repo_name = last_star.split('/')[1]
        last_star_with_link = f'<a href="https://github.com/{last_star}" style="color: inherit; text-decoration: none;"  target="blank">{last_star_repo_name}</a>'

    #----------------------------------------
    texts = [
        f" Right now, I'm diving into {latest_activity['repo_lang']}.",
        f'I’m currently working on my {working_on} project.',
        f" Ask me about {language_count[0]} and {language_count[1]}",
        f"{adieu(co_names)}",
        f" Just starred the amazing repository {last_star_repo_name} ! "
    ]

    # Calculate the height of the background box
    total_height = 20  # Initial padding
    wrapped_texts = []


    # Ensure total height doesn't exceed user-defined height
    total_height = min(total_height, height)

    # Set a top margin for the text
    margin = 20 * total_height // 100  # Adjust this value as needed


    svg_content = sample

    customs = {
        'bgcolor' : bgcolor,
        'width_custom' : str(width),
        'height_sutom' : str(height+ margin // 2), 
        'FONT_SIZE': str(font_size),
        'width_custom2': str(width - 5),
        'Header_Color' : str(header_color),
        'USERNAME_': username,

    }

    for key in customs:
        svg_content = svg_content.replace(key,customs[key])

    
    icons = [ROCKET,SEARCH_ALT,CHEF,GLASS,STAR]


    line_components = ""
    # Add wrapped texts to the SVG with top margin
    temp = " <text class=\"stat  bold\" x=\"25\" y=\"12.5\"> TEXT_FOR_LINE </text>"
    tspan = "<tspan x=\"25\" dy=\"yloc\"> TS_TEXT  </tspan>"
    count_line = 0
    for i,line in enumerate(texts):
        # svg_content += f'<text x="20" y="{margin + line_height * i}" class="text">{line}</text>\n'
        wrapped_lines = wrap_text(line, max_width, font_size)
        len_warp_line = len(wrapped_lines)
        count_line += len_warp_line

        line_ = f"<tspan x=\"25\" dy=\"0\">{wrapped_lines[0]}</tspan>"
        for i,l in enumerate(wrapped_lines[1:]):
            tspan_temp = tspan.replace("TS_TEXT",l)
            tspan_temp = tspan_temp.replace("yloc",f"{1.2}em")
            
            line_ += tspan_temp

        data_for_line = {
            "LINE_HERE": temp.replace("TEXT_FOR_LINE",line_),
            "icon_svg_sample":icons[i],
            "Ylocation":str((count_line)*25),
        }
        line_ = line_component
        for key in data_for_line:
            line_ = line_.replace(key,data_for_line[key])

        line_components += line_



    svg_content = svg_content.replace("LINE_COMPONENTS", line_components)

    svg_content = svg_content.replace(working_on,working_on_with_link)
    svg_content = svg_content.replace(last_star_repo_name,last_star_with_link)

    for x in co_names:
        svg_content = svg_content.replace(x,f'<a href="https://github.com/{x}" style="color: inherit; text-decoration: none;"  target="blank">{x}</a>')

    # print(svg_content)
    
    return HttpResponse(svg_content, content_type='image/svg+xml')
