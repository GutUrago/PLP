# Step 1: Read from input.txt
try:
    with open('input.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found in the directory.")

# Step 2: Count number of words
word_count = len(content.split())

# Step 3: Convert all text to uppercase
uppercase_content = content.upper()

# Step 4: Write to output.txt
with open('output.txt', 'w') as file:
    file.write(uppercase_content)
    file.write("\n\n")
    file.write(f"Word Count: {word_count}\n")

# Step 5: Print success message
print("✅ File 'output.txt' created successfully with processed text and word count.")
