"""Grading app"""

score = int(input("what is your score? "))

if score > 80:
  print("Excellent")
elif score > 60:
  print("Very Good")
elif score > 40:
  print("Good")
elif score > 20:
  print("Good")
else:
  print("Poor")