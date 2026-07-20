import time
t = time.strftime('%H:%M:%S')
hour = float(time.strftime('%H'))
print(hour)

if hour >= 0 and hour < 12:
    print("Good Morning Sir!")
elif hour >= 12 and hour < 16:
    print("Good Afternoon Sir!")
else:
    print("Good Night Sir!")        