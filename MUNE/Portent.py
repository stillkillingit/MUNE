# Create functions for Portent, Interventions, Portents, NPC Attitudes,
#    and TWENE.  Ideally, integrate these with a basic NPC generation 
from selenium import webdriver
import math
import random # a = random.randint(start,end)

class Portent():
    def portent_1(self):
       driver = webdriver.Chrome()
       driver.get('http://watchout4snakes.com/Random/RandomSentence')
       omen = driver.find_element_by_id('result').text
       driver.close()
       return omen

    # Function for importing number
    #def foreshadow(self, omen):
    #    return getattr(self, omen)()

# Creating the Portent object
trelawney = Portent()

# Verification
print(trelawney)
