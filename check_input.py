""" Set of functions to validate user input.

Written by: Shannon Cleary
Date: Fall 2022

Functions:
	get_int(prompt) - returns a valid integer (positive or negative).
	get_positive_int(prompt) - returns a valid positive (>=0) integer.
	get_int_range(prompt, low, high) - returns a valid integer within the inclusive range.
	get_float(prompt) - returns a valid decimal value.
	get_yes_no(prompt) - returns a valid yes/no input.

Usage: in your program, import the check_input module.  Then call one of the methods using check_input.

Example Usage:

	import check_input

	val = check_input.get_int("Enter #:")
	print(val)

"""

def get_int(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is an integer.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    The valid positive integer input.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be an integer.")
  return val


def get_positive_int(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is a positive (>= 0) integer.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    The valid integer input.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= 0:
        valid = True
      else:
        print("Invalid input - should not be negative.")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val  


def get_int_range(prompt, low, high):
  """Repeatedly takes in and validates user's input to ensure that it is an integer within the specified range.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
    low: lower bound of range (inclusive)
    high: upper bound of range (inclusive)
  Returns:
    The valid integer input within the specified range.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= low and val <= high:
        valid = True
      else:
        print("Invalid input - should be within range " + str(low) + "-" + str(high) + ".")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val


def get_float(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is a float.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    The valid floating point input.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = float(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be a decimal value.")
  return val


def get_yes_no(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is a yes or a no answer.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    True if yes, False if no.
  """
  valid = False
  while not valid:
    val = input(prompt).upper()
    if val == "YES" or val == "Y":
      return True
    elif val == "NO" or val == "N":
      return False
    else:
      print("Invalid input - should be a 'Yes' or 'No'.")
