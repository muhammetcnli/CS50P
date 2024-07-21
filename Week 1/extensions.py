file_name = input("File name: ").lower().strip()

last_name = ""

extension_index = 1

file_name_list = file_name.split(".")

if len(file_name_list) == 3:
    extension_index = 2

if len(file_name_list) == 1:
    last_name = "application/octet-stream"

elif file_name_list[extension_index] == "gif":
    last_name = "image/gif"

elif file_name_list[extension_index] == "jpg":
    last_name = "image/jpeg"

elif file_name_list[extension_index] == "jpeg":
    last_name = "image/jpeg"

elif file_name_list[extension_index] == "png":
    last_name = "image/png"

elif file_name_list[extension_index] == "pdf":
    last_name = "application/pdf"

elif file_name_list[extension_index] == "txt":
    last_name = "text/plain"

elif file_name_list[extension_index] == "zip":
    last_name = "application/zip"
else:
    last_name = "application/octet-stream"

print(last_name.strip("\n"))