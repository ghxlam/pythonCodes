class Dog:
    '''Ghulam Ahmed, CS100, 011, 11/23/2021, HW 11'''

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name+ ' knows ' + trick)

    def knows(self, trick):
        if trick in self.tricks:
            print('Yes, '+ self.name +' knows '+ trick)
            print('True')
        else:
            print('No, '+ self.name +' doesn\'t know '+ trick)
            print('False')

    species = 'Canis familiaris'
