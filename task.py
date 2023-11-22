class Task:
  """ Maintains a list of tasks for a user. 
    Attributes:
    description (str): string description of the task
    date (str): due date of the task. A string in the format: YYYY/MM/DD 
    time (str): time the task is due.  A string in the format: HH:MM """

  def __init__(self, desc, date, time):
    """ Assign the parameters to the attributes of the task."""
    self.description = desc
    self.date = date
    self.time = time

  def get_description (self):
    """ Returns the task’s description. """
    return self.description

  def __str__(self):
    """ Returns a string used to display the task’s information to the user. """
    return self.description + " - Due: " + self.date + " at: "+ self.time

  def __repr__(self): 
    """ Returns a string used to display the task’s information to the text file."""
    return self.description + "," + self.date + ","+ self.time + "\n"

  def __lt__(self, other):
    """ Returns true if the self task is less than the other task.  
Compare by year, then month, then day, then hour, then minute, and then the task description in alphabetical order. """
    
    date = self.date.split('/') #[year,month,date]
    time = self.time.split(':') #[hour,minute]
    otherDate = other.date.split('/')
    otherTime = other.time.split(':')
    if date[0] == otherDate [0]: #If years are equal
      if date[1] == otherDate[1]: #If months are equal
        if date[2] == otherDate[2]: #If days are equal
          if time[0] == otherTime[0]: #If hours are equal
            if time[1] == otherTime[1]: #If minutes are equal
              #then sort the list alphabetically
              return self.description < other.description
            return time[1] < otherTime[1]
          return time[0] < otherTime[0]
        return date[2] < otherDate[2]
      return date[1] < otherDate[1]
    return date[0] < otherDate[0]
    
