
class Home:
    def __init__(self, rollno, firstname, lastname, marks, course):
        self.rollno=rollno
        self.firstname=firstname
        self.lastname=lastname
        self.marks=marks
        self.course=course
        self.stinfo={'firstname':self.firstname, 'lastname':self.lastname, 'marks':self.marks , 'course':self.marks}
        self.fullinfo={rollno:self.stinfo}
        
    def command(self, x):
            return self.fullinfo[x]

    def __str__(self):
        return self.name
                



if __name__== "__main__" :
    y=1
    while(y):
      rollno=int(input("enter the roll number :"))
      firstname=input("enter the first name :")
      lastname=input("enter the lastname :")
      marks=input("enter the cgpa :")
      subject=input("enter the course name :")
      y=int(input("if you want more then press 1 otherwise enter 0 :"))


    student=Home(rollno, firstname, lastname, marks, subject)

    x=int(input("enter the roll number :"))

    info=student.command(x)
    print("so the first name: " ,info['firstname'])
    print("so the last name: " ,info['lastname'])
    print("so the marks is : " ,info['marks'])
    print("so the course : " ,info['course'])

