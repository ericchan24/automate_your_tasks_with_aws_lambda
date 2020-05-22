def get_links(soup_obj):
    '''
    gets all the links on the fangraphs blog page --> https://blogs.fangraphs.com/
    '''
    links = []
    for i, element in enumerate(soup_obj.find_all(class_='more-link', href = True), 1):
        links.append(element['href'])
    return links

def get_article_title(soup_obj):
    '''
    gets article title from a fangraphs article
    '''
    article_title = soup_obj.find('title').text.strip()
    return article_title

def get_article_date(soup_obj):
    '''
    gets article date from a fangraphs article
    '''
    article_metadata = soup_obj.find('div', class_ = 'postmeta')
    article_date = article_metadata.find_all('div')[-1].text
    return article_date

def get_article_text(soup_obj):
    '''
    gets article text from a fangraphs article
    '''
    full_post = soup_obj.find_all('div', class_ = 'fullpostentry')

    for tag in full_post:
        p_tags = tag.find_all("p")
        article_lst = []
        for p in p_tags:
            if len(p.text.strip()) > 0:
                article_lst.append(p.text)
    article_text = '\n\n'.join(article_lst)
    return article_text
