# Author: Vishal Munic vqm5223@psu.edu
# Collaborator: Bakhtiar Reza bmr5782@psu.edu 
# Collaborator: Claire Kessel cmk6318@psu.edu 
# Collaborator: Bakhtiar Reza bmr5782@psu.edu
# Section: 4
# Breakout: 10

def getLetterGrade(grade):
  if (grade >= 93):
    return "A"
  elif (grade >= 90):
    return "A-"
  elif (grade >= 87):
    return "B+"
  elif (grade >= 83):
    return "B"
  elif (grade >= 80):
    return"B-"
  elif (grade >= 77):
    return "C+"
  elif (grade >= 70):
    return "C"
  elif (grade >= 60):
    return "D"  
  else:
    return "F"

def run():
 grade = float(input("Enter your CMPSC 131 grade: "))
 
 print(f"Your letter grade for CMPSC 131 is {(getLetterGrade(grade))}.")

if __name__ == "__main__":
  run()