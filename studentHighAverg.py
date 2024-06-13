# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

  howmnaystudent=0
# Write your code below this row 👇
for numberofstudent in student_heights:
  totalhight=+student_heights
  howmnaystudent+=1

averghig=totalhight/howmnaystudent
print(f'total height ={totalhight}')
print(f'number of students ={howmnaystudent}')
print(f'average height ={averghig}')


  
