#meal time
# 7:00 - 8:00 breakfast
#12:00 - 13:00 lunch
#18:00 - 19:00 dinner

def main():
    time=input("what time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    time = hours + minutes
    return time

if __name__ == "__main__":
    main()
