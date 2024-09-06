name = input("Enter Your Name : ")
cost = float(input("Enter Cost of the Product : "))
qty = float(input("Enter Quantity of the Product : "))
amount = cost * qty
gst = 12 *  amount / 100
total = amount + gst

if total < 1000:
  discount = 0
elif total < 3000:
  discount = 0.1 * total
else:
  discount = 0.2 * total

print("Amount is : ",amount)
print("GST is : ",gst)
print("Discount is : ",discount)
print("Amount to be paid : ",total - discount)
