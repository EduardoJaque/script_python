s=input("camelCase: ")
new_s = ""
for c in s:
    if c.isupper():
        new_s += "_"
    new_s += c
new_s= new_s.lower()
print("snake_case:",new_s)