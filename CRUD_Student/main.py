from module import *


def Main():
  exit = False
  studentslist = []
  
  while not exit:
    
    option = CRUDStudentsMenu()
    
    match option:
    
      case 0: # Exit
        exit = True

        print("\nGOOD BYE!!!")
      case 1: # Create
        studentslist.append(CreateStudent())
      case 2: # Read
        StudentPrintAll(studentslist)
      case 3: # Uptade
        UpdateStudent(studentslist)
      case 4: # Delete
        DeleteStudent(studentslist)
      case _: # Input ERROR
        print ("\n!!!TYPE A VALID NUMBER!!!\n");

if __name__ == "__main__":
  Main()