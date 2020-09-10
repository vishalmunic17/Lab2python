# Author: Vishal Munic vqm5223@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 
# Breakout:


 

def getLetterGrade(grade):
  if (grade >= 93):
    print ("Your letter grade for CMPSC 131 is A.")
  elif (grade >= 90):
    print("Your letter grade for CMPSC 131 is A-.")
  elif (grade >= 87):
    print("Your letter grade for CMPSC 131 is B+.")
  elif (grade >= 83):
    print("Your letter grade for CMPSC 131 is B.")
  elif (grade >= 80):
    print("Your letter grade for CMPSC 131 is B-.")
  elif (grade >= 77):
    print("Your letter grade for CMPSC 131 is C+.")
  elif (grade >= 70):
    print("Your letter grade for CMPSC 131 is C.")
  elif (grade >= 60):
    print("Your letter grade for CMPSC 131 is D.")  
  else:
    print("Your letter grade for CMPSC 131 is F.")

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  getLetterGrade(grade)

if __name__ == "__main__":  run()