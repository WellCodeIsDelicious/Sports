import requests
from bs4 import BeautifulSoup

# Fetch HTML content
url = 'https://soccer.freesportstime.com/'
response = requests.get(url)
html_content = response.content

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract names and links
names_links = {}
sections = soup.find_all('ul', class_='list-group')
for section in sections:
    section_name = section.find('center').text.strip()
    links = section.find_all('li', class_='list-group-item')
    names_links[section_name] = {link.text.strip(): link.a['href'] for link in links}

# Now, 'names_links' holds the extracted data
# You can format this data and update your .m3u8 file
# For instance, write the content to a new .m3u8 file
with open('updated_file.m3u8', 'w') as file:
    for section, data in names_links.items():
        file.write(f"# {section}\n")
        for name, link in data.items():
            file.write(f"{name},{link}\n")
