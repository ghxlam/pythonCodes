class Section:
    '''sections in a school'''
    def __init__(self,section_id):
        self.section_id = section_id
        self.enrolled_students = []
        
    def enroll(self, stu_name):
        self.enrolled_students.append(stu_name)
        
    def is_enrolled(self,stu_name):
        return stu_name in self.enrolled_students
