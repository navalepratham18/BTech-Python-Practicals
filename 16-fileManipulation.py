with open("textfile.txt", "w") as file:
    file.write("Hello, World!")

with open("textfile.txt", "r") as file:
    print("Read Text File:", file.read())

with open("textfile.txt", "a") as file:
    file.write("\nAppended text.")

with open("textfile.txt", "r") as file1, open("copyfile.txt", "w") as file2:
    file2.write(file1.read())

with open("binaryfile.bin", "wb") as file:
    file.write(b"Binary content here.")

with open("binaryfile.bin", "rb") as file:
    print("Read Binary File:", file.read())
