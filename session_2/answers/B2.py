# B2
# i   - Ask the user to enter their age
# ii  - If they are younger than 11, print "You're too young to go to this school"
# iii - If they are between 11 and 16, print "You can come to this school"
# iv  - If they are over 16, print "You're too old for school"
# v   - If they are 0, print "You're not born yet!"

age = int(input("How old are you?\n"))

if age < 11:
    print("You're too young to go to this school")
elif age >= 11 and age <= 16:
    print("You can come to this school")
elif age > 16:
    print("You're too old for school")
elif age == 0:
    print("You're not born yet")
else:
    print("You didn't pick a number")
