
def checkDriverAge():
    age = input("input your age:")
if int (age) < 18:
    print("sorry, you are too young to operate this vehicle")
elif int(age) > 18:
    print("AUTOBOTS, ROLLOUT!!!!")
elif int(age) == 18:
    print("Congrats on reaching 18 years, lets roll!")
    
checkDriverAge(18)
