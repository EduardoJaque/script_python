
x=input("input: ")
n=""
k=["a","e","o","i","u","A","E","I","O","U"]
for i in x:
    if i not in k:
        n+=i
print(n)
