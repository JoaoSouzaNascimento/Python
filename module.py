
class Person:
  def __init__(self, name, naid, day, month, year, sex):
    self.name = name
    self.naid = naid
    self.birth = FormatDate(day, month, year)
    self.sex = sex

  def Name(self, name):
    self.name = name
    
  def NacinalID(self, naid):
    self.naid = naid

  def DateBirth(self, day, month, year):
    self.birth = FormatDate(day, month, year)

  def Sex(self, sex):
    self.sex = sex

  def GetName(self):
    return self.name

  def GetNacinalID(self):
    return self.naid

  def GetDateBirth(self):
    return self.birth

  def GetSex(self):
    return self.sex

class Student(Person):
  def __init__(self, name, naid, day, month, year, sex, inid):
    self.name = name
    self.naid = naid
    self.birth = FormatDate(day, month, year)
    self.sex = sex
    self.inid = inid
  
  def InstitutionalID(self, inid):
    self.inid = inid

def FormatDate(day, month, year):
  return str(year) + str(month).zfill(2) + str(day).zfill(2)

def CreateStudent():
  name = InputName()
  naid =  InputNaID()
  year = InputYear()
  month = InputMonth()
  day = InputDay()
  sex = InputSex()
  inid = InputInID()
  
  student = Student(name,naid,day,month,year,sex,inid)

  return student

def StudentPrint(student):
  print("NAME: {}".format(student.name))
  print("CPF: {}".format(student.naid))
  print("DATE OF BIRTH: {}/{}/{}".format(student.birth[7:8],
                                        student.birth[6:5],
                                        student.birth[0:4]))
  print("INSTITUTIONAL ID: {}".format(student.naid))
  print("SEX: {}\n".format(student.naid))
  

def StudentPrintAll(studentslist):
  print("\nALL STUDENTS LIST:\n")
  if len(studentslist)==0:
    print("!!!EMPTY!!!")
  for student in studentslist:
    StudentPrint(student)


def DeleteStudent(studentslist):
  studentid = InputInID()
  
  for student in studentslist:
    if studentid == student.inid:
      print("STUDENT DOES NOT EXIST")
      return studentslist.remove(student)
    print("SUCCESS")

def UpdateStudent(studentslist):
  studentid = InputInID()
  exit = False
  option = 0
  for student in studentslist:
    if studentid == student.inid:
      while not exit:
        option = MenuUpdate()

        match option:
          case 0:
            exit = True
            return
          case 1:
            student.name = InputName()
          case 2:
            student.naid = InputNaID()
          case 3:
            day = InputDay()
            month = InputMonth()
            year = InputYear()
            student.birth = FormatDate(day, month, year)
          case 4:
            student.sex = InputSex()
          case _:
            print("!!!TYPE A VALID NUMBER!!!")
            
def MenuUpdate():
  print('[0] -> EXIT')
  print('[1] -> STUDENT NAME')
  print('[2] -> STUDENT CPF ')
  print('[3] -> STUDENT DATE OF BYTH')
  print('[4] -> STUDENT SEX\n')

  return int(input("TYPE A NUMBER >>> "))
  
def InputName():
  print("\nENTER THE STUDENT NAME:")
  return input(">>> ")

def InputNaID():
  print("\nENTER THE STUDENT CPF (JUST THE NUMBERS):")
  return input(">>>")

def InputDay():
  print("\nENTER THE STUDENT DAY OF BIRTH:")
  return int(input(">>>"))

def InputMonth():
  print("\nENTER THE STUDENT MONTH OF BIRTH:")
  return int(input(">>>"))

def InputYear():
  print("\nENTER THE STUDENT YEAR OF BIRTH:")
  return int(input(">>>"))

def InputSex():
  print("\nENTER THE STUDENT SEX:")
  return input(">>>")

def InputInID():
  print("\nENTER THE STUDENT INSTITUTIONAL ID:")
  return input(">>>")

def CRUDStudentsMenu():
  print('[0] -> EXIT')
  print('[1] -> REGISTER STUDENTS')
  print('[2] -> LIST STUDENTS')
  print('[3] -> UPDATE STUDENTS')
  print('[4] -> DELETE STUDENTS \n')

  return int(input("TYPE A NUMBER >>> "))