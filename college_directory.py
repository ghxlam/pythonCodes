class CollegeDirectory:
    '''represents a collegeDirectory'''

    def __init__(self, name):
        self.name = name
        self.students= {}

    def addStudent(self, studentName, emailAddress):
        self.students[studentName] = emailAddress

    def getEmailList(self):
        lst= []
        for student in self.students:
            lst.append(student+ ' <'+self.students[student]+'> ')
        return lst
