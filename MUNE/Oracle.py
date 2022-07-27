# Create functions for Oracle, Interventions, Portents, NPC Attitudes,
#    and TWENE.  Ideally, integrate these with a basic NPC generation 

import random # a = random.randint(start,end)

class Oracle():
    def oracle_1(self):
        print('No, and...')
    def oracle_2(self):
        print('No.')
    def oracle_3(self):
        print('No, but...')
    def oracle_4(self):
        print('Yes, and...')
    def oracle_5(self):
        print('Yes.')
    def oracle_6(self):
        print('Yes, but...')

    # Function for importing number
    def foretell(self, oracles):
        #i = 0   #  This will be for when it automatically gives up to 3 answers.
            #  Max number of Yes, buts or No, buts is 3.
            #  Stop at Yes or No
            #  Third iteration is only Yes or No
        answer1 = 'oracle_' + str(oracles)

# Creating the Oracle object
delphi = Oracle()

# Verification
#a = random.randint(1,6)
#delphi.foretell(a)
