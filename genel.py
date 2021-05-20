# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
from os.path import join as pjoin

#Create project directory
def create_webpage_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    print("\n{0} directory is created. \n".format(directory))

#Create crawded html files
def create_html_files(path,file_name,url):
    source_code = requests.get(url)
    plain_text = source_code.text
    path_to_file = pjoin(path,file_name)
    print("{0} is created".format(path_to_file))
    with open(path_to_file, 'w') as file:
        file.write(str(plain_text))

#Create crawled text files
def create_text_files(path,file_name,url):
    source = requests.get(url)
    soup = BeautifulSoup(source.content, "html.parser")
    content = soup.find("article", class_='ue-c-article')
    title = content.h1.get_text()
    article = content.findAll('p')
    path_to_file = pjoin(path, file_name)
    print("{0} is created".format(path_to_file))
    with open(path_to_file, 'w') as file:
        file.write(str(title).upper() + "\n\n")
        for text in article:
            file.write(text.text + "\n")




