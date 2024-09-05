name= input("Enter name : ")
eng = float(input("Enter marks in English : "))
math = float(input("Enter marks in Math : "))
sci = float(input("Enter marks in Science : "))
sst = float(input("Enter marks in SST : "))

total = eng + math + sci + sst
per = total / 5

print("==============================")
print("Report card For",name)
print("Total Marks Scored ",total)
print("Percentage Marks",per,"%")
if per >= 40:
  print("Congratulation !!!")
else:
  print("Sorry, Better Luck")
print("===============================")
