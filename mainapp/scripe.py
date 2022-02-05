from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

vuz_inf_dict = {
	"Число публикаций на elibrary.ru" : 0,
	"Число публикаций в РИНЦ" : 0,
	"Число публикаций, входящих в ядро РИНЦ" : 0,
	"Число цитирований публикаций на elibrary.ru" : 0,
	"Число цитирований публикаций в РИНЦ" : 0,
	"Число цитирований из публикаций, входящих в ядро РИНЦ" : 0,
	"Индекс Хирша по всем публикациям на elibrary.ru" : 0,
	"Индекс Хирша по публикациям в РИНЦ" : 0,
	"Индекс Хирша по ядру РИНЦ" : 0,
	"g-индекс" : 0,
	"i-индекс" : 0,
	"Число авторов" : 0,
	"Число авторов, зарегистрированных в Science Index" : 0
}

sotrud_inf_dict = {
	"Число публикаций на elibrary.ru" : 0,
	"Число публикаций в РИНЦ" : 0,
	"Число публикаций, входящих в ядро РИНЦ" : 0,
	"Число цитирований из публикаций на elibrary.ru" : 0,
	"Число цитирований из публикаций, входящих в РИНЦ" : 0,
	"Число цитирований из публикаций, входящих в ядро РИНЦ" : 0,
	"Индекс Хирша по всем публикациям на elibrary.ru" : 0,
	"Индекс Хирша по публикациям в РИНЦ" : 0,
	"Индекс Хирша по ядру РИНЦ" : 0,
}

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
		vuz_inf_dict["Число публикаций на elibrary.ru"] = items[0].text

	items = soup.find_all('a', attrs={'title':'Список публикаций организации в РИНЦ'})
	if items[0].text:
		vuz_inf_dict["Число публикаций в РИНЦ"] = items[0].text

	items = soup.find_all('a', attrs={'title':'Список публикаций организации, входящих в ядро РИНЦ'})
	if items[0].text:
		vuz_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = items[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Число цитирований публикаций на elibrary.ru":
				td_num = n
	vuz_inf_dict["Число цитирований публикаций на elibrary.ru"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Число цитирований публикаций в РИНЦ":
				td_num = n
	vuz_inf_dict["Число цитирований публикаций в РИНЦ"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Число цитирований из публикаций, входящих в ядро РИНЦ":
				td_num = n
	vuz_inf_dict["Число цитирований из публикаций, входящих в ядро РИНЦ"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Индекс Хирша по всем публикациям на elibrary.ru":
				td_num = n
	vuz_inf_dict["Индекс Хирша по всем публикациям на elibrary.ru"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Индекс Хирша по публикациям в РИНЦ":
				td_num = n
	vuz_inf_dict["Индекс Хирша по публикациям в РИНЦ"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Индекс Хирша по ядру РИНЦ":
				td_num = n
	vuz_inf_dict["Индекс Хирша по ядру РИНЦ"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "g-индекс":
				td_num = n
	vuz_inf_dict["g-индекс"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "i-индекс":
				td_num = n
	vuz_inf_dict["i-индекс"] = items[td_num + 1].find_all('font')[0].text

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Число авторов":
				td_num = n
	vuz_inf_dict["Число авторов"] = items[td_num + 1].find_all('font')[0].text


	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Число авторов":
				td_num = n
	vuz_inf_dict["Число авторов, зарегистрированных в Science Index"] = items[td_num + 4].find_all('font')[0].text

def sotrud_obsh_inf(soup):
	items = soup.find_all('a', attrs={'title':'Полный список публикаций автора на портале elibrary.ru'})
	try:
		sotrud_inf_dict["Число публикаций на elibrary.ru"] = items[0].text
	except IndexError:
		sotrud_inf_dict["Число публикаций на elibrary.ru"] = 0

	items = soup.find_all('a', attrs={'title':'Список публикаций автора в РИНЦ'})
	try:
		sotrud_inf_dict["Число публикаций в РИНЦ"] = items[0].text
	except IndexError:
		sotrud_inf_dict["Число публикаций в РИНЦ"] = 0

	items = soup.find_all('a', attrs={'title':'Список публикаций данного автора, входящих в ядро РИНЦ'})
	try:
		sotrud_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = items[0].text
	except IndexError:
		sotrud_inf_dict["Число публикаций, входящих в ядро РИНЦ"] = 0

	items = soup.find_all('a', attrs={'title':'Список цитирований публикаций автора на elibrary.ru'})
	try:
		sotrud_inf_dict["Число цитирований из публикаций на elibrary.ru"] = items[0].text
	except IndexError:
		sotrud_inf_dict["Число цитирований из публикаций на elibrary.ru"] = 0

	items = soup.find_all('a', attrs={'title':'Список цитирований публикаций автора в РИНЦ'})
	try:
		sotrud_inf_dict["Число цитирований из публикаций, входящих в РИНЦ"] = items[0].text
	except IndexError:
		sotrud_inf_dict["Число цитирований из публикаций, входящих в РИНЦ"] = 0

	items = soup.find_all('a', attrs={'title':'Список цитирований публикаций автора по ядру РИНЦ'})
	try:
		sotrud_inf_dict["Число цитирований из публикаций, входящих в ядро РИНЦ"] = items[0].text
	except IndexError:
		sotrud_inf_dict["Число цитирований из публикаций, входящих в ядро РИНЦ"] = 0

	items = soup.find_all('td')
	td_num = 0
	for n, i in enumerate(items, start=0):
		tags = i.find_all('font')
		for j in tags:
			if j.text == "Индекс Хирша по всем публикациям на elibrary.ru":
				td_num = n
	sotrud_inf_dict["Индекс Хирша по всем публикациям на elibrary.ru"] = items[td_num + 1].find_all('font')[0].text
	sotrud_inf_dict["Индекс Хирша по публикациям в РИНЦ"] = items[td_num + 4].find_all('font')[0].text
	sotrud_inf_dict["Индекс Хирша по ядру РИНЦ"] = items[td_num + 7].find_all('font')[0].text

def vuz_inf(orgId):
	str_url = "https://www.elibrary.ru/org_profile.asp?id=" + str(orgId)
	soup = scripe(str_url)
	vuz_obsh_inf(soup)

def sotrud_inf(authorId):
	str_url = "https://elibrary.ru/author_profile.asp?authorid=" + str(authorId)
	soup = scripe(str_url)
	sotrud_obsh_inf(soup)
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
