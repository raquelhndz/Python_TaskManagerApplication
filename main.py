# Raquel Hernandez and Alice Huynh 
# 2/21/2023
# Task List
import task
import check_input
def main_menu():
  """ Displays main menu and returns the users choice. """
  
  userChoice = check_input.get_int_range("1. Display Current Task\n2. Mark current task compelete\n3. Postpone current task\n4. Add new task\n5. Save and quit\nEnter Choice: ",1,5)
  return userChoice

def read_file(filename):
  """ Reads in tasks from file and creates an object of lists that contains each task. """
  tasklist = open(filename)
  list = tasklist.readlines()
  objList = []
  for line in list: # ['desc', 'date', 'time']
    line = line.strip('\n')
    splitList = line.split(',')
    objList.append(task.Task(splitList[0], splitList[1], splitList[2]))

  return objList

def write_file(filename,objList):
  """ Writes back to the file using repr. """
  tasklist = open(filename, "w")
  for i in objList:
    tasklist.writelines(repr(i)) 
  tasklist.close()
  
  
def get_date():
  """ Gets date in formatted form for the user to update and create new tasks. Returns year, month, day as 3 variables. """
  
  print("\n*Enter due date*")
  dueYear = check_input.get_int_range("Enter year: ",2000,3000)
  dueMonth = check_input.get_int_range("Enter month: ",1,12)
  dueMonth = format(dueMonth,'02d')
  dueDay = check_input.get_int_range("Enter day: ",1,31)
  dueDay = format(dueDay,'02d')
  return dueYear, dueMonth, dueDay
  
def get_time():
  """ Gets time in formatted form to update hour and minutes. """
  dueHour = check_input.get_int_range("Enter hour: ",0,23)
  dueHour = format(dueHour,'02d')
  dueMinute = check_input.get_int_range("Enter minute: ",0,59)
  dueMinute = format(dueMinute,'02d') 
  return dueHour, dueMinute


  
def main():
  filename = "tasklist.txt"
  objList = read_file(filename)
  objList.sort()
  while True:
    print()
    print("--Task List--")
    if len(objList)!=0:
      print("Taks to complete:",len(objList))
    else:
      print("Task to complete: 0")
    userChoice = main_menu()
    
    if userChoice == 1: # display current task 
      if len(objList)!=0:
        print("Current task is:")
        print(objList[0])
      else:
        print("No current task. Task list is empty. ")
      
     
      
    if userChoice == 2: # delete current task 
      if len(objList)!=0:
        print("Marking current task as complete:")
        print(objList[0])
        del objList[0]
        if len(objList)!=0:
          print("New current task is:")
          print(objList[0])
        objList.sort()
      else:
        print("No current task. Task list is empty. ")
      
      
    if userChoice == 3: #postpone current task, update date and time
      if len(objList)!=0:
        print("Postponing task: \n" + str(objList[0]))
        print("Enter new due date:")
        updatedTask_year, updatedTask_month, updatedTask_day = get_date()
        update_dueDate = format(str(updatedTask_year)+"/"+str(updatedTask_month)+"/"+str(updatedTask_day))
        print("Enter new time:")
        updatedTask_hour, updatedTask_minute = get_time()
        update_dueTime = format(str(updatedTask_hour)+":"+str(updatedTask_minute))
        postpone_Taskname = objList[0].get_description()
        del objList[0]
        objList.append(task.Task(postpone_Taskname, update_dueDate, update_dueTime))
        objList.sort()
      else:
         print("No current task. Task list is empty. ")
        
    if userChoice == 4: #create a new task 
      newTask = input("Enter a task description: ")
      newTask_year, newTask_month, newTask_day = get_date()
      newTask_dueDate = format(str(newTask_year)+"/"+str(newTask_month)+"/"+str(newTask_day))
      
      newTask_hour, newTask_minute = get_time()
      newTask_dueTime = format(str(newTask_hour)+":"+str(newTask_minute))
      
      objList.append(task.Task(newTask,newTask_dueDate,newTask_dueTime))
      objList.sort()
      
    if userChoice == 5: #write to txt file and close
      
      write_file(filename, objList)
      print(" Done. ")
      break
  
  
  
main()



