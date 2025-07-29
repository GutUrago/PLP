# Try opening the file

file_name = input("File Name: ")

# Try to open the file
try:
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:
    print(f"{file_name} doesn't exist in the directory.")

# Ask for input text
input_text = input("What do you want to append?")

# Append the text

with open(file_name, 'a') as file:
    file.write("\n")
    file.write(input_text)

print(f"✅ {input_text} has been successfully appended to {file_name}.")
