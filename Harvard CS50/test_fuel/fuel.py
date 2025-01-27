def main():
    x=input("Fraction: ")
    convert(x)

def convert(fraction):

    fraction=fraction.split("/")
    fraction1=int(fraction[0])
    fraction2=int(fraction[1])
    if fraction1>fraction2:
        raise ValueError
    elif fraction2==0:
        raise ZeroDivisionError
    elif fraction1<fraction2:
        i=(fraction1/fraction2)*100
        return round(i)
def gauge(percentage):
    if 0<= percentage<2 or 98<percentage<100:
        match percentage:
            case 0:
                return ("E")
            case 1:
                return ("E")
            case 100:
                return ("F")
            case 99:
                return ("F")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()