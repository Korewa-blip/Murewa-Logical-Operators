medical_cause=input("Do you have a medical cause Y or N:")
annt=int(input("Please Enter the Attendance:"))
if medical_cause=='Y':
 print("You are allowed")
else:
 if annt>=75:
  print("You are allowed")
 else:
  print("Not allowed")