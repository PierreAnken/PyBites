from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')

    book_title = soup.find('h2').text.strip()
    book_summary = soup.find('div', {'class': 'dotd-main-book-summary float-left'})
    book_description = book_summary.find_all('div')[2].text.strip()
    book_image_block = soup.find('div', {'class': 'dotd-main-book-image float-left'})
    book_image_url = book_image_block.find('img').attrs.get('src')
    book_link = book_image_block.find('a').attrs.get('href')
    return Book(book_title, book_description, book_image_url, book_link)
