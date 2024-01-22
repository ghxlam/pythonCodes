class State:
    '''Represents a state'''

    def __init__(self, name):
        self.name = name
        self.universities = []

    def add_university(self, univName):
        self.universities.append(univName)

    def is_home_of(self, uName):
        if uName in self.universities:
            return True
        else:
            return False
