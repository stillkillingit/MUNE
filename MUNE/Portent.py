# Create functions for Portent, Interventions, Portents, NPC Attitudes,
#    and TWENE.  Ideally, integrate these with a basic NPC generation 
from requests_html import HTMLSession

class Portent():
    def portent_1(self):
       session = HTMLSession()
       r = session.get('http://watchout4snakes.com/Random/RandomSentence')
       
       # Add sleep time; default is not long enough
       r.html.render(sleep=0.5)
       omen = r.html.fine('#result', first=TRUE).text
       return omen

# Creating the Portent object
trelawney = Portent()

# Verification
print(trelawney)
