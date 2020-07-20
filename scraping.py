# Import Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup as soup
import pandas as pd


# Windows users path
# The browser now belongs to Splinter for the duration of our coding

executable_path = {'executable_path': 'chromedriver_win32.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Section 10.3.3 Scrape Mars Data: The News

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the HTML
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# Scrape the Title
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# Section 10.3.4 Scrape Mars Data: Featured Images

# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# Section 10.3.5 Scrape Mars Data: Mars Facts

df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()

# Section 10.3.6 Export to Python




