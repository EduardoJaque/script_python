x=input("File name: ")
if ".gif" in x:
    print("image/gif")
elif ".jpg" in x:
    print("image/jpeg")
elif ".jpeg" in x:
    print("image/jpeg")
elif ".png" in x:
    print("image/png")
elif ".zip" in x:
    print("application/zip")
elif ".pdf" in x:
    print("application/pdf")
elif  "PDF" in x:
    print("application/pdf")
elif ".txt" in x:
    print("text/plain")
else:
    print("application/octet-stream")