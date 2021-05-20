import crawler

website = input('Enter website(www.elmundo.es) name: ')
crawling_depth = input('Enter crawling depth: ')
store_type = input('Press 1 to store raw-html file or 2 to store txt file: ')
root_folder = input('Enter root folder which you want to save(C:/Example/):')

crawler.web_crawler(website, int(crawling_depth), int(store_type), root_folder)