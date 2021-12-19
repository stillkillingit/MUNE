# Create functions for Portent, Interventions, Portents, NPC Attitudes,
#    and TWENE.  Ideally, integrate these with a basic NPC generation 

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Portent():

    def Omen(self):
        
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-sh-usage')
        path = Service('C:\\Users\\Ross\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe')
        driver = webdriver.Chrome(service=path, options=option)
        #driver = webdriver.Firefox()
        url = 'http://watchout4snakes.com/Random/RandomSentence'
        driver.get(url)
        omen = driver.find_element(By.ID,"result").text

        return omen

    def __repr__(self) -> str:
        return self.Omen()

# Creating the Portent object
trelawney = Portent()

# Verification
print(trelawney)
