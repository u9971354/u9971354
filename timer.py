# IMPORTANT
# This is a smart timer made by Jaydev for you with 🧠🤯 

from datetime import datetime
import time
#------------------------------------------------------------------------------------------------
end_statement = "____________________________________________________________________________________________________________________________________________"
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#------------------------------------------------------------------------------------------------
def reset():
  flag = input(f"Do you want to start timer again? ({timer_hours}:{timer_minutes}:{timer_seconds} Reply ('Yes' / 'No') : ").upper()
#------------------------------------------------------------------------------------------------
def confirmation1(question):
  reply = str(input(question))
  if reply.upper() == "EXIT":
    exit()
  elif reply.upper() == "RESET":
    reset()
  elif reply.upper() == "RESTART":
    timer()
  else:
    for i in range(5):
      print()
    question = "Enter '0' to stop and '1' to restart : "
    confirmation1(question)
  print()  
#------------------------------------------------------------------------------------------------
def confirmation(timer_hours, timer_minutes, timer_seconds):
  flag = input(f"Do you want to set timer to {timer_hours}:{timer_minutes}:{timer_seconds}? ('Yes' / 'No') : ").upper()
  if flag == "YES":
    flag= True
  elif flag == "NO":
    flag= False
  else:
    for i in range(5):
      print()
    confirmation(timer_hours, timer_minutes, timer_seconds)
  return flag
  print()  
#------------------------------------------------------------------------------------------------
def gettime():
  current_datetime = str(datetime.now()).replace("."," ").split()
  current_date = current_datetime[0].replace("-", " ").split()
  current_time = current_datetime[1].replace(":"," ").split()
  current_datetime = current_date + current_time 
  return current_datetime
#------------------------------------------------------------------------------------------------
def calculate_timer_end(timer_hours, timer_minutes, timer_seconds):
  current_year = int(gettime()[0])
  current_month = int(gettime()[1])
  current_date = int(gettime()[2])
  current_hour = int(gettime()[3])
  current_minute = int(gettime()[4])
  current_second = int(gettime()[5])
  timer_end_year = current_year
  timer_end_month = current_month
  timer_end_date = current_date
  timer_end_hour = current_hour + timer_hours
  timer_end_minute = current_minute + timer_minutes
  timer_end_second = current_second + timer_seconds
#------------------------------------------------------------------------------------------------
  while timer_end_second > 59:
    timer_end_second -= 60
    timer_end_minute += 1
  while timer_end_minute > 59:
    timer_end_minute -= 60
    timer_end_hour += 1
  while timer_end_hour > 23:
    timer_end_hour -= 24
    timer_end_date += 1
  while timer_end_date > month_days[current_month - 1]:
    timer_end_date -= month_days[current_month - 1]
    timer_end_month += 1
  while timer_end_month > 12:
    timer_end_month -= 12
    timer_end_year += 1 
  if timer_end_hour > 12:
    timer_end_hour -= 12
    am_pm = "PM"
  else:
    am_pm = "AM"
#------------------------------------------------------------------------------------------------
  str(timer_end_year)
  str(timer_end_month)
  str(timer_end_date)
  str(timer_end_hour)
  str(timer_end_minute)
  str(timer_end_second)
#------------------------------------------------------------------------------------------------
  if timer_end_date == current_date:
    timer_end = f"{timer_end_hour}:{timer_end_minute}:{timer_end_second} {am_pm}"
  else:
    timer_end = f"{timer_end_hour}:{timer_end_minute}:{timer_end_second} {am_pm} ({timer_end_date}/{timer_end_month}/{timer_end_year})"
  return timer_end
#------------------------------------------------------------------------------------------------
def isleapyear():
  current_year = int(gettime()[0])
  if current_year % 4 == 0:
    month_days[1] = 29
  else:
    month_days[1] = 28
#------------------------------------------------------------------------------------------------
def timer():
  global  timer_seconds, timer_minutes, timer_hours
  print(end_statement)
  for i in range(5):
    print()
  i = True
  while i == True:
    try:
      i = False
      timer_seconds = int(input("Enter second(s) between 0-59 for timer : "))
      if timer_seconds > 59:
        timer_seconds = 59
      elif timer_seconds < 0:
        timer_seconds = 0
      print(f"Timer seconds set to {timer_seconds}")
    except:
      i = True
      print("Please enter number(s) only.")
      for i in range(5):
        print()
  print()
#------------------------------------------------------------------------------------------------
  i = True
  while i == True:
    try:
      i = False
      timer_minutes = int(input("Enter minute(s) between 0-59 for timer : "))
      if timer_minutes > 59:
        timer_minutes = 59
      elif timer_minutes < 0:
        timer_minutes = 0
      print(f"Timer minutes set to {timer_minutes}")
    except:
      i = True
      print("Please enter number(s) only.")
      for i in range(5):
        print()
  print()
#------------------------------------------------------------------------------------------------
  i = True
  while i == True:
    try:
      i = False
      timer_hours = int(input("Enter hour(s) for timer : "))
      if timer_hours < 0:
        timer_hours = 0
      print(f"Timer hours set to {timer_hours}")
    except:
      i = True
      print("Please enter number(s) only.")
      for i in range(4):
        print()
  print()
#------------------------------------------------------------------------------------------------
  timer_duration = timer_hours*3600 + timer_minutes*60 + timer_seconds
  flag = confirmation(timer_hours, timer_minutes, timer_seconds)
  timer_end = calculate_timer_end(timer_hours, timer_minutes, timer_seconds)
  if flag:
    for i in range(5):
      print()
    print(f"Timer started! It will go of on {timer_end}")
    time.sleep(timer_duration)
    for i in range(5):
      print()
    question = "Time's up! Enter 'Exit' to exit, 'Reset' to reset or 'Restart' to restart : "
    confirmation1(question)
  elif not flag:
    print("Enter again")
    timer()
#------------------------------------------------------------------------------------------------
isleapyear()
timer()
