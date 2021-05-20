# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import genel

def web_crawler(web_url,crawl_depth, store_type, root_folder):

    path = root_folder + web_url
    try:
        genel.create_webpage_dir(path)
        news_number = 1
        if store_type == 1:
            filename = 'main.html'
            genel.create_html_files(path, filename, 'https://' + web_url)

            if crawl_depth == 1:
                links = link_finder(web_url)
                for link in links:

                    filename = 'news' + str(news_number) + '.html'
                    genel.create_html_files(path, filename, link)
                    news_number += 1
                print('\n {0} html files are created'.format(news_number-1))

        if store_type == 2:
            if crawl_depth == 0:
                print("Main web page does not have news text!")
            if crawl_depth == 1:
                links = link_finder(web_url)
                for link in links:
                    try:

                        filename = 'news' + str(news_number) + '.txt'
                        genel.create_text_files(path, filename, link)
                        news_number += 1
                    except:
                        pass

                print('{0} text files are created'.format(news_number-1))

    except requests.exceptions.ConnectionError:
        print('You dont have internet connection or the webpage does not exist ')
    except OSError:
        print('Creation of the directory %s is failed' % path)

def link_finder(url):

    source=requests.get('https://'+url)
    soup=BeautifulSoup(source.content,"html.parser")
    content=soup.find("main")
    linkler = content.find_all("a")
    link_list=[]
    for link in linkler:
        if str(link.get("href")).startswith('https://'+url):
            link_list.append(link.get("href"))
        #link_list=[ln for ln in link_list if not ln.startswith('#')]#Listeden # ile baslayanlar cıkarılacak
    return link_list