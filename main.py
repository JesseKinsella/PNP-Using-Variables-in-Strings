day = 7
month = 'March'
temp = 40

print("Today is March 7 and it's 40 degrees outside")

#use variables with f string
print(f"Today is March 7 and it's 40 degrees outside") #putting the f makes this still valid

print(f"Today is March {day} and it's 40 degrees outside") #use curly brackets with f-string, nice!

print(f"Today is {month} {day} and it's {temp} degrees outside")

day_name = 'Monday'

print(f"Today is {day_name}, {month} {day}, and it's {temp} degrees outside")