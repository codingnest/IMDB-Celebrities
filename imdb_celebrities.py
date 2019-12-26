from bs4 import BeautifulSoup
import urllib.request

if __name__ == '__main__':
    page_url = "http://m.imdb.com/feature/bornondate"
    #Accessing the HTML content from the webpage
    with urllib.request.urlopen(page_url) as response:
        page = response.read()

    #Parsing the HTML Content
    soup = BeautifulSoup(page, 'html.parser')
    details = soup.find_all('div', class_='lister-item mode-detail')
    celebrities_details = {}
    for i in range(10):
        celebrities_details[i] = {}
        for row in details[i].findAll('div', attrs = {'class':'lister-item-image'}):
            celebrities_details[i]['name'] = row.img['alt']
            celebrities_details[i]['image'] = row.img['src']
        for row in details[i].findAll('div', attrs = {'class': 'lister-item-content'}):
            celebrities_details[i]['movie'] = row.select('[href*="title"]')[0].getText()
    for key in celebrities_details:
        print(celebrities_details[key]['name'], celebrities_details[key]['movie'], celebrities_details[key]['image'])