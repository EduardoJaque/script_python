print("Amount Due: 50")
i=50
while True:
    x=int(input("Insert Coin: "))
    if x ==25 or x==10 or x==5:
        if i>=x:
            i=i-x
            print("Amount Due:",i)
            if i==0:
                print("Change Owed:",i)
                break
        elif x>i:
            j=x-i
            print("Change Owed:",j)
            i=i-x
            if i<=0:
                break
    elif x !=25 or x!=10 or x!=5:
        print("Amount Due: 50")
        x=int(input("Insert Coin: "))



