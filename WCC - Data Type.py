

# Task 1: Sum of integers in a list
print("Task 1: Sum of integers in a list")
user_input = input("Enter integers separated by spaces: ")
numbers = list(map(int, user_input.split()))
print(f"The sum of the numbers is: {sum(numbers)}")
print("-" * 40)

# Task 2: Tuple of favorite books
print("Task 2: Favorite books (using tuple)")
favorite_books = ("Sapiens", "1984", "Atomic Habits", "The Alchemist", "Thinking, Fast and Slow")
for book in favorite_books:
    print(book)
print("-" * 40)

# Task 3: Dictionary of personal info
print("Task 3: Personal info dictionary")
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")

print("\nPersonal Information:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
print("-" * 40)

# Task 4: Common elements between two sets
print("Task 4: Common elements in two sets")
set1 = set(map(int, input("Enter first set of integers (space-separated): ").split()))
set2 = set(map(int, input("Enter second set of integers (space-separated): ").split()))
common_elements = set1 & set2
print(f"Common elements: {common_elements}")
print("-" * 40)

# Task 5: List comprehension for words with odd number of characters
print("Task 5: Words with odd number of characters")
words = ["apple", "banana", "pear", "kiwi", "grape", "plum", "mango"]
odd_length_words = [word for word in words if len(word) % 2 == 1]
print("Words with odd lengths:")
print(odd_length_words)
