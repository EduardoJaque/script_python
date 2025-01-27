greeting=input("Greeting: ")
if "What's happening" in greeting or "What's up" in greeting:
    print("$100")

elif "Hello" in greeting or "hello" in greeting:
    print("$0")
elif  "H" in greeting or "h" in greeting:
    print("$20")
else:
    print("$100")