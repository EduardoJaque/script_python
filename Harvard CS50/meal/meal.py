def main():
    hora=input("what time is it? ")

    if 7<=convert(hora)<=8:
        print("breakfast time")
    elif 12<=convert(hora)<=13:
        print("lunch time")
    elif 18<=convert(hora)<=19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours=float(hours)
    minutes=float(minutes)
    return (((hours*60)+minutes)/60)

if __name__ == "__main__":
    main()



