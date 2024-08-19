from django.shortcuts import render
from django.http import HttpResponse
from .functions import *

def adieu(names):
    num_names = len(names)
    if num_names == 1:
        return (f"🤝 I recently collaborated with {names[0]}.")
    elif num_names == 2:
        return (f"🤝 I recently collaborated with {names[0]} and {names[1]}.")
    else:
        output = "🤝 I recently collaborated with "
        for i in range(num_names):
            if i == num_names - 1:
                pass
            elif i == num_names - 2:
                output += f"{names[i]}, and {names[i+1]}."
            else:
                output += f"{names[i]}, "
        return (output)


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')

    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '{:02x}{:02x}{:02x}'.format(*rgb)

def get_complementary_color(hex_color):
    rgb = hex_to_rgb(hex_color)
    comp_rgb = (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])
    return rgb_to_hex(comp_rgb)

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

def svg_generator(request,username):
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
    repo_languages = {'Captcha-breaker': 'Python', 'Data-Structure-Coursera': 'C#', 'Emergency-pm': 'CSS', 'friendZone': 'Jupyter Notebook', 'images': 'Jupyter Notebook', 'MalwareDetector': 'Python', 'Petro-Lithology-Prediction': 'Jupyter Notebook', 'quera-solutions': 'Python', 'Stratego': 'Java', 'Sudoku_cpp': 'C++', 'Toos': 'Python', 'webShop': 'Python', 'Web_Security_tools': 'Python', 'words': 'Python', 'xv6-public': 'C'}

    language_count = list(count_repos_by_language(repo_languages))


    latest_activity = {'type': 'PushEvent', 'repo_name': 'Seyedsahel/ProfilePizza',
      'repo_url': 'https://api.github.com/repos/Seyedsahel/ProfilePizza', 'repo_lang': 'Python'}
    #----------------------------------------
    # repo_languages = get_repo_languages(username)
    # print(repo_languages)
    # print(f"--------------------")


    # language_count = list(count_repos_by_language(repo_languages))
    # print(language_count)
    # print(f"--------------------")

    # latest_activity = get_latest_activity(username)
    # print(latest_activity)
    #----------------------------------------

    co_name , working_on = latest_activity['repo_name'].split('/')
    working_on_with_link = f'<a href="https://github.com/{latest_activity["repo_name"]}">{working_on}</a>'

    # co_names = get_user_contributors(username)

    texts = [
        f"🚀 Right now, I'm diving into {latest_activity['repo_lang']}.",
        f'🔧 I’m currently working on my {working_on} project.',
        f"📚  Ask me about {language_count[0]} and {language_count[1]}",
        # f"{adieu(co_names)}",
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

    # print(svg_content)
    return HttpResponse(svg_content, content_type='image/svg+xml')
