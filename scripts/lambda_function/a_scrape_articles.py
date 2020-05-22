from bs4 import BeautifulSoup
import datetime
import lxml
import os
import requests
import utils

def main():
    '''
    scrapes all of today's articles on https://blogs.fangraphs.com/
    '''
    # get the links to all the articles
    url = 'https://blogs.fangraphs.com/'
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "lxml")
    links = utils.get_links(soup)

    # if an article was written today, save it
    today_datetime = datetime.datetime.now().date()
    article_title_lst = []
    article_date_lst = []
    article_text_lst = []

    for link in links:
        response = requests.get(link)
        page = response.text
        soup = BeautifulSoup(page, "lxml")
        article_date = utils.get_article_date(soup)
        article_date_datetime = datetime.datetime.strptime(article_date,
            '%B %d, %Y').date()
        if today_datetime == article_date_datetime:
            article_title = utils.get_article_title(soup)
            article_text = utils.get_article_text(soup)
            article_title_lst.append(article_title)
            article_date_lst.append(article_date)
            article_text_lst.append(article_text)

    title = f'articles_{today_datetime}'.replace('-', '_')

    return article_title_lst, article_date_lst, article_text_lst

if __name__ == '__main__':
    main()
