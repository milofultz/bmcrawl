from bs4 import BeautifulSoup
import random
import requests
from requests.exceptions import ConnectionError
import webbrowser

def bm_input_handler(filename):
    with open(filename, 'r') as f:
        html = f.read()
    
    print('Scraping bookmark file...')
    urls = scrape(html, 'bookmarks.html')
    
    return urls

def url_input_handler():
    urls = []

    #for as long as the user wants to add URLs
    while True:
        url = input('Enter a full URL (include http://) --> ')
        #if user is all done
        if not url.strip():
            break
        else:
            url_tuple = (url, url, 'User Input')
            urls.append(url_tuple)
    
    #send back usable data
    return urls

bad_links = ['facebook.com', 'twitter.com', 'instagram.com', 'mailto:', 'wiki']

def scrape(html, from_title):

    url_list = []

    soup = BeautifulSoup(html, 'html.parser')

    for i, link in enumerate(soup.find_all('a')):
        
        link_url = link.get('href')
        
        if i >= 50:
            print(link_url + ' has too many links.')
            break
        
        if link_url == None \
        or any(substring in link_url for substring in bad_links) \
        or '//' not in link_url:
            continue 
        url_list.append((link.text, link_url, from_title))

    return url_list


def crawler(start_urls, depth=1):
    found_urls = []

    for n in range(depth):
        print(f'Crawling at depth {n}...')
        new_urls = crawl(start_urls)
        found_urls.append(new_urls)
        start_urls = new_urls

    print('Crawl completed!')
    return found_urls


def crawl(start_urls):
    found_urls = []
    
    for title, link, _ in start_urls:
        html = getpage(link)
        if html == None:
            continue
        found_urls.extend(scrape(html, title))

    return found_urls


def getpage(url):
    try:
        response = requests.get(url)
    except ConnectionError:
        return
    html = response.text

    return html


def chrome(address):
    """ Opens given URL in Chrome. """
    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(address)


header = '<html><body><ul>'
footer = '</ul></body></html>'

def output_handler(urls, number):
    random.shuffle(urls)
    
    with open(f'newlinks_{number}.html', 'w') as f:
        f.write(header)
        for title, url, from_title in urls:
            if title.isspace() or title == '':
                title = url
            f.write(f'<li><a href="{url}" target="_blank">{title} - {url} <i>({from_title})</i></a></li>')
        f.write(footer)

    chrome(f'newlinks_{number}.html')


if __name__ == '__main__':

    depth = int(input('How deep? 1 is good, and 2 is plenty. --> '))

    #ask user to choose between bookmarks.html or URL input
    input_type = input('Bookmarks (b) or URLs (u)? --> ')
    
    #if user wants to input URLs
    if input_type.lower() == 'u':
        #run url input handler
        start_urls = url_input_handler()
    else:
        bm = 'bookmarks.html'
        start_urls = bm_input_handler(bm)
    
    #crawl URLs and output to list of tuples
    found_urls = crawler(start_urls, depth)

    for i, urls_list in enumerate(found_urls):
        output_handler(urls_list, i)