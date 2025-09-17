from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"
file_path_2 = workspace / "missing_files.txt"
print(file_path)

# # f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# # f.write("This file will only be created if it doesn't exist.\n")
# # f.close()

# f = open(file_path, "w", encoding="utf-8")
# f.write("Shopping List:\n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()

# f = open(file_path, "a", encoding="utf-8")
# f.write(" - Groundnut oil\n")
# f.write(" - Maggi\n")
# f.write(" - Water\n")
# f.close()

# Read the whole file
# f = open(file_path, "r", encoding="utf-8")
# for line in f:
#     print("->", line.rstrip())
# f.close()

# with open(file_path, "a", encoding="utf-8") as f:
#     f.write(" - Salt\n")
#     f.write(" - Sugar\n")

# with open(file_path, "r+", encoding="utf-8") as f:
#     # f.write(" - Soda\n")
#     # f.write(" - Onion\n")
#     for line in f:
#         print("->", line.rstrip())
# try:
#     with open(workspace / "missing_files.txt", "r", encoding="utf-8") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("The file does not exist.")
#     print("Creating the file now...")

#     # Now create the file
#     with open(workspace / "missing_files.txt", "w") as f:
#         f.write("This file was created because it was missing.\n")
#     print("File created succesfully")

if file_path_2.exists():
    print(f"Found the file: {file_path_2.name}")

    # Get some information about the file
    file_size = file_path_2.stat().st_size
    print(f"File size: {file_size} bytes")
    print("--" * 10)

    with open(file_path_2, "r", encoding="utf-8") as f:
        content = f.readline()
        print(f"Content preview:\n{content}")
else:
    print(f"The file {file_path_2.name} does not exist.")

# function call 
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)
# https://www.mediafire.com/file/issqx7q0rgkwpuv/w3schools_Offline_2020.zip/file
