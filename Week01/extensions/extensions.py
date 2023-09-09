formats = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg" : "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}

input = input("File name: ").strip().lower()

if input.rfind(".") != -1:
    index = int(input.rindex(".")) + 1
    input = input[index:]

    if input not in formats:
        print("application/octet-stream")
    else:
        print(formats[input])

else:
    print("application/octet-stream")