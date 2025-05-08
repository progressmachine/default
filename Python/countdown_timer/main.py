import time

hours = int(input("Enter Hours: "))
minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter Seconds: "))

hours_s = hours*3600
minutes_s = hours_s + minutes*60
seconds = minutes_s + seconds

for i in range(seconds, 0, -1):
    minutes = int(i / 60)
    seconds = int(i % 60)

    hours = int(minutes/60)
    minutes = int(minutes % 60)

    print(f"> {hours:02}:{minutes:02}:{seconds:02}", end = "\r")
    time.sleep(1)

print("Time's Up!")