# vkr

pip install Django
pip install beautifulsoup4
pip install selenium

-----------------------  1 ------------------------------
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
---------------------------------------------------------
-----------------------  2 -----------------------------------------------------------------
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
--------------------------------------------------------------------------------------------

python manage.py runserver
