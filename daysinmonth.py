def is_leap(year):
  """To check if it is a leap year, enter the year in parentheses."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """To find out how many days a month is, enter the year in parentheses first, then the month with a comma."""
  if month > 12 and month < 1:
      return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) == False:
    return month_days[month - 1]
  else:
      if month == 2:
          return 29
      else:
          month_days[month - 1]
  
 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)