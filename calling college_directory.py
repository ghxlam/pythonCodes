import college_directory
myDirectory= college_directory.CollegeDirectory('Hawthorne')
myDirectory.addStudent('Hester Prynne', 'hprynne@hawthorne.edu')
myDirectory.addStudent('Roger Chillingworth', 'rchillingworth@hawthorne.edu')
print(myDirectory.getEmailList())
