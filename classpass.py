


percentclass=80

firstexam=50
secondexam=60
thirdexam=80

exampass=firstexam*0.2+secondexam*0.3+thirdexam*0.5

passclass=exampass>=65 and percentclass>=80

print("Student passed the class", passclass)

