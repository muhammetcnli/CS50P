file_name = input("File name: ")

last_name = ""

file_name_list = file_name.split(".")

if len(file_name_list) == 1:
    last_name = "application/octet-stream"
elif file_name_list[1] == "gif":
    last_name = "image/gif"
elif file_name_list[1] == "jpg":
    last_name = "image/jpg"
elif file_name_list[1] == "jpeg":
    last_name = "image/jpeg"
elif file_name_list[1] == "png":
    last_name = "image/png"
elif file_name_list[1] == "pdf":
    last_name = "application/pdf"
elif file_name_list[1] == "txt":
    last_name = "text/plain"
elif file_name_list[1] == "zip":
    last_name = "application/zip"

print(last_name)