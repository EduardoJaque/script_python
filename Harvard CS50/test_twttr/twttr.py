def main():
    x=input("input: ").title()
    print(shorten(x))

def shorten(word):
    n=""
    k=["a","e","o","i","u","A","E","I","O","U"]
    for i in word:
        if i not in k:
            n+=i
    return n
if __name__ == "__main__":
    main()