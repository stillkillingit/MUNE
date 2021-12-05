# Interventions - 

import random # a = random.randint(start,end)

class Intervention():
    def insert_1(self):
        print('New Entity')
    def insert_2(self):
        print('Entity positive')
    def insert_3(self):
        print('Entity negative')
    def insert_4(self):
        print('Advance plot')
    def insert_5(self):
        print('Regress plot')
    def insert_6(self):
        print('Wild')

    # Function for importing number
    def mediate(self, inserts):
        answer = 'insert_' + str(inserts)
        return getattr(self, answer)()

# Creating the Intervention object
saint = Intervention()

# Verification
a = random.randint(1,6)
saint.mediate(a)
