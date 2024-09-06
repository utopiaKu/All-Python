"""  a leap year is, occurring once every four years, which has 366 days including 29 February as an intercalary day """

year = int(input("Enter the year to be checked : "))

if year % 100 == 0:
  if year % 400 == 0:
    print(year, "is not a leap year")
  else:
    print(year, "is not a leap year")
else:
  if year % 4 == 0:
    print(year, "is a leap year")
  else:
    print(year, "is not a leap year")
