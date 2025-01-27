def main():
    greeting=input("Greeting:")
    print(f"${value(greeting)}")

def value(greeting):

    x=""
    if "What's happening" in greeting or "What's up" in greeting:
        x=100

    elif "Hello" in greeting or "hello" in greeting:
        x=0
    elif  "H" in greeting or "h" in greeting:
        x=20
    else:
        x=100
    return(x)

if __name__ == "__main__":
    main()