
class Person:
  def __init__(self, name, naid, day, month, year, sex):
    self.name = name
    self.naid = naid
    self.birth = FormatDate(day, month, year)
    self.sex = sex

class Student(Person):
  def __init__(self, name, naid, day, month, year, sex, inid):
    super().__init__(name, naid, day, month, year, sex)
    self.inid = inid


def FormatDate(day, month, year):
  return str(year) + str(month).zfill(2) + str(day).zfill(2)

def CreateStudent(studentslist):
  name = InputName()
  naid =  InputNaID(studentslist)
  year = InputYear()
  month = InputMonth()
  day = InputDay(month, year)
  sex = InputSex()
  inid = InputInID(studentslist)
  
  student = Student(name,naid,day,month,year,sex,inid)

  return student

def MenuStudentPrint():
  print("\nSTUDENT LISTS OPTIONS (TYPE THE NUMBER):\n")
  print("[0] -> EXIT")
  print("[1] -> LIST IN ALPHABETICAL ORDER")
  print("[2] -> LIST BY AGE")

  return input(">>> ")
  
def PrintStudent(studentslist):
  if len(studentslist)==0:
    return print("\n!!!THE LIST OF STUDENTS IS EMPTY!!!\n")
    
  while True:
    option = MenuStudentPrint()

    match option:
      case '0':
        return
        
      case '1':
        StudentPrintAll(SortAlphabetical(studentslist))
      case '2':
        StudentPrintAll(SortByAge(studentslist))
      case _:
        print("!!!TYPE A VALID NUMBER!!!")

def SortByAge(list):
  return sorted(list, key=lambda list: list.birth)

def SortAlphabetical(list):
  return sorted(list, key=lambda list: list.name)
  
def StudentPrint(student):
  print("NAME: {}".format(student.name))
  print("CPF: {}".format(student.naid))
  print("DATE OF BIRTH: {}/{}/{}".format(student.birth[6:8],
                                        student.birth[4:6],
                                        student.birth[0:4]))
  print("INSTITUTIONAL ID: {}".format(student.inid))
  print("SEX: {}\n".format(student.sex))
  

def StudentPrintAll(studentslist):
  print("\nALL STUDENTS LIST:\n")
  
  if len(studentslist)==0:
    print("!!!EMPTY!!!")
    
  for student in studentslist:
    StudentPrint(student)


def DeleteStudent(studentslist):
  studentid = InputInID(studentslist)
  
  for student in studentslist:
    if studentid == student.inid:
      print("STUDENT DOES NOT EXIST")
      return studentslist.remove(student)
    print("SUCCESS")

def UpdateStudent(studentslist):
  if len(studentslist)==0:
    return "\n!!!THE LIST OF STUDENTS IS EMPTY!!!\n"
  
  studentid = InputInID(studentslist)
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
            student.naid = InputNaID(studentslist)
          case 3:
            year = InputYear()
            month = InputMonth()
            day = InputDay(month, year)
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
  while True:
    try:
      print("\nENTER THE STUDENT NAME:")
      name = input(">>> ")

      if(not name.isdigit()):
        break

      print("\n!!!TYPE A VALID NAME!!!\n")
      
    except Exception as error:
      print("\n!!!ERROR: {} !!!\n".format(error))
      
  return name

def IsCPFValid(cpf):
  digit = 10
  cpfvalid = 0
  if len(cpf) == 11 and cpf.isdigit():
    for i in range(2):
      for j in range(9+i):
        cpfvalid += int(cpf[j]) * (digit - j)
        
      
      cpfvalid = (cpfvalid * 10) % 11
      
      if cpfvalid == 10:
        cpfvalid = 0
  
      if cpfvalid != int(cpf[9+i]):
        return False
      else:
        digit = 11
        cpfvalid = 0
        
  else:
    return False
        
  return True
  
def InputNaID(studentslist):
  while True:
    try:
      print("\nENTER THE STUDENT CPF (JUST THE NUMBERS):")
      cpf = input(">>> ")
      

      if IsCPFValid(cpf):
        if not any(cpf == student.naid for student in studentslist):
          break
          
        else: 
          print("\n!!!CPF ALREADY EXISTS!!!\n")
      else:
        print("\n!!!TYPE A VALID CPF!!!\n")
    
    except Exception as error:
      print("\n!!!ERROR: {} !!!\n".format(error))
  
  return cpf

def IsLeapYear(year):
  if(year % 100 != 0 and year%4==0 or year%400 ==0):
    return True
    
  return False
  
def InputDay(month, year):
  months = [31,28,31,30,31,30,31,31,30,31,30,31]
  
  if(IsLeapYear(year)):
    months[1] = 29

  currentday = months[month-1]
  
  while True:
    print("\nENTER THE STUDENT DAY OF BIRTH:")
    
    try:
      day = int(input(">>> "))
      
      if(0<day<=currentday):
        break
      else:
          print("\n!!!TYPE A NUMBER BETWEEN 1 AND {}!!!".format(months[month-1]))
        
    except ValueError:
      print("\n!!!TYPE A VALID NUMBER!!!")

  return day

def InputMonth():
  currentmonth = 12
  while True:
    print("\nENTER THE STUDENT MONTH OF BIRTH:")
    try:
      month = int(input(">>> "))

      if(0<month<=currentmonth):
        break
      else:
        print("\n!!!TYPE A NUMBER BETWEEN 1 AND 12")
    
    except ValueError:
      print("\n!!!TYPE A VALID NUMBER!!!")
  
  return month

def InputYear():
  currentyear = 2023
  while True:
    print("\nENTER THE STUDENT YEAR OF BIRTH:")
    try:
      year = int(input(">>> "))

      if(1850<year<=currentyear):
        break
      else:
        print("\n!!!TYPE A VALID YEAR!!!")

    except ValueError:
      print("\n!!!TYPE A VALID NUMBER!!!")

  return year

def InputSex():
  print("\nENTER THE STUDENT SEX (TYPE DE NUMBER):\n")
  print("[0] -> I'D RATHER NOT ANSWER")
  print("[1] -> MASCULINE")
  print("[2] -> FEMININE")
  print("[3] -> OTHER\n")

  while True:
    option = input(">>> ")

    match option:
      case '0':
        return "I'D RATHER NOT ANSWER"
      case '1':
        return "MASCULINE"
      case '2':
        return "FEMININE"
      case '3':
        return "OTHER"
      case _:
        print("!!!TYPE A VALID NUMBER!!!")

def InputInID(studentslist):
  while True:
    try:
      print("ENTER THE STUDENT INSTITUTIONAL ID:\n")
      inid = input(">>> ")

      if inid.isdigit() and len(inid)==11:
        if not any(inid == st.inid for st in studentslist):
          break
        else:
          print("\n!!!EXISTS INSTITUTIONAL ID ALREADY!!!\n")

      print("\n!!!TYPE A VALID INSTITUTIONAL ID!!!\n")

    except Exception as error:
      print("\n!!!ERROR: {} !!!\n".format(error))

  return inid

def CRUDStudentsMenu():
  
  print('\n[0] -> EXIT')
  print('[1] -> REGISTER STUDENTS')
  print('[2] -> LIST STUDENTS')
  print('[3] -> UPDATE STUDENTS')
  print('[4] -> DELETE STUDENTS \n')

  return input("TYPE A NUMBER >>> ")