from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def scripe(url):
#	s=Service(ChromeDriverManager().install())
#	driver = webdriver.Chrome(service=s)
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--incognito')
	options.add_argument('--headless')
	driver = webdriver.Chrome("C:/Users/Alexandr/Documents/chromedriver/chromedriver.exe", chrome_options=options)
	driver.get(url)
	time.sleep(1)
	page_source = driver.page_source
	soup = BeautifulSoup(page_source, 'lxml')
	return soup
	
def find_author_name(soup):
	items = soup.find_all('div')
	div_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('span', class_='aster')
		for j in tags:
			if j.text=='*':
				div_num = n
	return items[div_num].find('b').text
	
def find_vuz_name(soup):
	items = soup.find_all('div')
	div_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('span', class_='aster')
		for j in tags:
			if j.text=='*':
				div_num = n
	return items[div_num].find('a').text
	
def find_kolvo_publ(soup):
	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Всего найдено":
				td_num = n
	return items[td_num].find_all('font')[1].text
	
def find_publ(soup):
	items = soup.find_all('span', attrs={'style':'line-height:1.0;'})
	span_num = 0
	return items[span_num].text

def vuz_obsh_inf(soup):
	items = soup.find_all('a', attrs={'title':'Список публикаций организации на портале elibrary.ru'})
	if items[0].text:
		return items[0].text
	else:
		return ""

def vuz_inf(orgId):
	str_url = "https://www.elibrary.ru/org_profile.asp?id=" + str(orgId)
	soup = scripe(str_url)
	return vuz_obsh_inf(soup)

#def main(args):
#	url = 'https://elibrary.ru/author_items.asp?authorid=640991'
#	soup = scripe(url)
#	print('Автор: ' + find_author_name(soup))
#	print('ВУЗ: ' + find_vuz_name(soup))
#	print('Всего публикаций: ' + find_kolvo_publ(soup))
#	print('Публикация 1: ' + find_publ(soup))

#if __name__ == '__main__':
#    import sys
#    sys.exit(main(sys.argv))
