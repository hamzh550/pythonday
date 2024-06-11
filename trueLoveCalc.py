print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
comabinams=name1+name2
comabinams=comabinams.lower()

countt=comabinams.count("t")
countr=comabinams.count("r")
countu=comabinams.count("u")
counte=comabinams.count("e")

number1=countt+countr+countu+counte

countl=comabinams.count("l")
counto=comabinams.count("o")
countv=comabinams.count("v")
counte=comabinams.count("e")
number2=countl+counto+countv+counte

finalnummber= (str(number1) +str( number2))
finalnummberint=int(finalnummber)

if finalnummberint <10 or finalnummberint >90:
  print(f"Your score is {finalnummberint}, you go together like coke and mentos.")

elif finalnummberint >=40 and finalnummberint <=50:
  print(f"Your score is {finalnummberint}, you are alright together.")

else :
  print(f"Your score is {finalnummberint}.")