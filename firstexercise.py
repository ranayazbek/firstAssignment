age = int(input("Please enter your age:"))
if age <= 5:
   ticket =0
   print (" you get in for free!")
elif age <= 10:
   ticket = 5
   print (" The ticket price is ", ticket)
elif age <= 16:
   ticket = 10
   print (" The ticket price is ", ticket)
else: 
   ticket = 15
   print (" The ticket price is ", ticket)

   