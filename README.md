# vkr

pip install Django <br/>
pip install beautifulsoup4 <br/>
pip install selenium <br/>
pip install webdriver-manager <br/>

https://github.com/mozilla/geckodriver/releases/ <br/>
tar -xvzf geckodriver* <br/>
sudo chmod +x geckodriver <br/>
sudo mv geckodriver /usr/local/bin/ <br/>

-----------------------  1 ------------------------------ <br/>
s=Service(ChromeDriverManager().install()) <br/>
driver = webdriver.Chrome(service=s) <br/>
-----------------------  2 ----------------------------------------------------------------- <br/>
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options) <br/>

python manage.py runserver
