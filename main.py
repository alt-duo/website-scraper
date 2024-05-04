import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
    response = requests.get(url, timeout=3, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to fetch the webpage.")
        return None

# Function to scrape links from HTML content
def scrape_links(html_content):
    if html_content is None:
        return []

    links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all <a> tags
    for link in soup.find_all('a'):
        # Extract the href attribute if it exists
        href = link.get('href')
        if href:
            links.append(href)
    return links



file = open('hours.txt', 'a') 

# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# year = str(input("Enter the year for your PVSA application: ")) 
year = "2024"
html_content = fetch_html("https://aylus.org/branches/san-diego-ca/")
if html_content:
    links = scrape_links(html_content)
    for link in links:
        file.write(link) 
        file.write("\n")
file.close()

file1 = open('hours.txt', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
f2 = open('right.txt','a')
for line in Lines:
    count += 1
    s = line.strip()
    t = s
    length = len(s)
    if length >= 20:
        if s[-3:] != "jpg":
            if s[18] == year[0]:
                if s[19] == year[1]:
                    if s[20] == year[2]:
                        if s[21] == year[3]:
                            
                            f2.write(t)
                            f2.write("\n")
soup1 = BeautifulSoup(html_content, 'html.parser')
soup1.get_text()