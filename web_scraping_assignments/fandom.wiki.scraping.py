import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the webpage
url = 'https://iceandfire.fandom.com/wiki/POV_characters'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract book titles (assuming this part is already working)
books_section = soup.find('div', {'class': 'wds-is-not-scrollable wds-dropdown-level-nested__content'})
book_titles = []
if books_section:
    books = books_section.find_all('a', {'data-tracking': 'custom-level-3'})
    for book in books:
        title = book.find('span').text.strip()
        book_titles.append(title)
print("Book Titles:", book_titles)

# Step 2: Fetch the new webpage for sample chapters
url2 = 'https://iceandfire.fandom.com/wiki/The_Winds_of_Winter'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')

# Step 3: Locate the section containing sample chapters
samplechapter_section = soup2.find('span', {'id': 'Viewpoint_characters'}).find_next('ul')

# Extract names and sample chapters
samplechapters = []
if samplechapter_section:
    items = samplechapter_section.find_all('li')
    for item in items:
        # Extract character name
        character_name = item.find('a').text.strip()
        # Extract number of sample chapters
        sample_chapters_text = item.text.strip()
        sample_chapters_count = sample_chapters_text.split(':')[0].strip().split()[0]
        samplechapters.append((character_name, sample_chapters_count))

# Print the results
print("W.O.W Sample Chapters:", samplechapters)

# Write the data to a CSV file
with open('/Users/alexguzman/Desktop/is310-coding-assignments/sample_chapters.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header
    csvwriter.writerow(['George R.R. Martin Sample Chapters and Novels'])
    
    # Write a section for book titles
    csvwriter.writerow(['Book Titles'])
    for title in book_titles:
        csvwriter.writerow([title])
    
    # Add a blank row for separation
    csvwriter.writerow([])
    
    # Write a section for sample chapters
    csvwriter.writerow(['Character Name', 'Sample Chapters'])
    csvwriter.writerows(samplechapters)
