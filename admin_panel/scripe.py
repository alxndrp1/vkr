from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

sot_inf = {
	"publ_rinc" : 0,
	"publ_yrinc" : 0,
	"cit_rinc" : 0,
	"hir_rinc" : 0,
	"2017_publ_rinc" : 0,
	"2017_publ_yrinc" : 0,
	"2017_cit_rinc" : 0,
	"2018_publ_rinc" : 0,
	"2018_publ_yrinc" : 0,
	"2018_cit_rinc" : 0,
	"2019_publ_rinc" : 0,
	"2019_publ_yrinc" : 0,
	"2019_cit_rinc" : 0,
	"2020_publ_rinc" : 0,
	"2020_publ_yrinc" : 0,
	"2020_cit_rinc" : 0,
	"2021_publ_rinc" : 0,
	"2021_publ_yrinc" : 0,
	"2021_cit_rinc" : 0,
	"2022_publ_rinc" : 0,
	"2022_publ_yrinc" : 0,
	"2022_cit_rinc" : 0,
}

options = Options()
options.headless = False
driver = 0

def dr_close():	
	global driver
	driver.close()

def autoriz():	
	global driver
	driver = webdriver.Firefox(options=options)
	driver.get("https://elibrary.ru")
	time.sleep(15)

def scripe(url):
	global driver
	driver.get(url)
	#time.sleep(1)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	if turing(soup):
		time.sleep(30)
		driver.get(url)
		#time.sleep(1)
		soup = BeautifulSoup(driver.page_source, 'lxml')
	return soup	

def turing(soup):
	if soup.find("img", {"src": "/images/robot2.png"}):
		return 1
	else:
		return 0

def p_hir_rinc(soup):
	items = soup.find_all('font')
	for i in items:
		if i.text == "Индекс Хирша по публикациям в РИНЦ":
			sot_inf["hir_rinc"] = int(i.find_next("font").text)					
			break

def p_publ_rinc(soup, year):
	publ_rinc = 0
	items = soup.find_all('font')
	for i in items:
		if i.text == "Всего найдено":
			publ_rinc = int(i.find_next("b").text)		
			break
		if i.text == "Всего найдена":
			publ_rinc = int(i.find_next("b").text)			
			break		
	if year == 0:
		sot_inf["publ_rinc"] = publ_rinc
	elif year == 1:
		sot_inf["2017_publ_rinc"] = publ_rinc
	elif year == 2:
		sot_inf["2018_publ_rinc"] = publ_rinc
	elif year == 3:
		sot_inf["2019_publ_rinc"] = publ_rinc
	elif year == 4:
		sot_inf["2020_publ_rinc"] = publ_rinc
	elif year == 5:
		sot_inf["2021_publ_rinc"] = publ_rinc
	elif year == 6:
		sot_inf["2022_publ_rinc"] = publ_rinc

def p_cit_rinc(soup, year):
	cit_rinc = 0
	items = soup.find_all('font')
	for i in items:
		if i.text == "Всего найдено":
			cit_rinc = int(i.find_next("b").text)					
			break
		if i.text == "Всего найдена":
			cit_rinc = int(i.find_next("b").text)			
			break				
	if year == 0:
		sot_inf["cit_rinc"] = cit_rinc
	elif year == 1:
		sot_inf["2017_cit_rinc"] = cit_rinc
	elif year == 2:
		sot_inf["2018_cit_rinc"] = cit_rinc
	elif year == 3:
		sot_inf["2019_cit_rinc"] = cit_rinc
	elif year == 4:
		sot_inf["2020_cit_rinc"] = cit_rinc
	elif year == 5:
		sot_inf["2021_cit_rinc"] = cit_rinc
	elif year == 6:
		sot_inf["2022_cit_rinc"] = cit_rinc	

def p_publ_yrinc(soup, year):
	publ_yrinc = 0
	items = soup.find_all('font')
	for i in items:
		if i.text == "Всего найдено":
			publ_yrinc = int(i.find_next("b").text)					
			break
	if year == 0:
		sot_inf["publ_yrinc"] = publ_yrinc
	elif year == 1:
		sot_inf["2017_publ_yrinc"] = publ_yrinc
	elif year == 2:
		sot_inf["2018_publ_yrinc"] = publ_yrinc
	elif year == 3:
		sot_inf["2019_publ_yrinc"] = publ_yrinc
	elif year == 4:
		sot_inf["2020_publ_yrinc"] = publ_yrinc
	elif year == 5:
		sot_inf["2021_publ_yrinc"] = publ_yrinc
	elif year == 6:
		sot_inf["2022_publ_yrinc"] = publ_yrinc

def sotrud_inf(authorId):
	soup = scripe("https://www.elibrary.ru/author_profile.asp?authorid=" + str(authorId))
	p_hir_rinc(soup)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0")
	p_publ_rinc(soup, 0)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId))
	p_cit_rinc(soup, 0)
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2")
	p_publ_yrinc(soup, 0)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&pubyear=2017")
	p_publ_rinc(soup, 1)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&sourceyear=2017")
	p_cit_rinc(soup, 1)	
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2&pubyear=2017")
	p_publ_yrinc(soup, 1)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&pubyear=2018")
	p_publ_rinc(soup, 2)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&sourceyear=2018")
	p_cit_rinc(soup, 2)	
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2&pubyear=2018")
	p_publ_yrinc(soup, 2)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&pubyear=2019")
	p_publ_rinc(soup, 3)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&sourceyear=2019")
	p_cit_rinc(soup, 3)	
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2&pubyear=2019")
	p_publ_yrinc(soup, 3)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&pubyear=2020")
	p_publ_rinc(soup, 4)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&sourceyear=2020")
	p_cit_rinc(soup, 4)	
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2&pubyear=2020")
	p_publ_yrinc(soup, 4)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&pubyear=2021")
	p_publ_rinc(soup, 5)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&sourceyear=2021")
	p_cit_rinc(soup, 5)	
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2&pubyear=2021")
	p_publ_yrinc(soup, 5)

	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=0&pubyear=2022")
	p_publ_rinc(soup, 6)
	soup = scripe("https://www.elibrary.ru/author_refs.asp?authorid=" + str(authorId) + "&sourceyear=2022")
	p_cit_rinc(soup, 6)	
	soup = scripe("https://elibrary.ru/author_items.asp?authorid=" + str(authorId) + "&pubrole=100&show_option=2&pubyear=2022")
	p_publ_yrinc(soup, 6)