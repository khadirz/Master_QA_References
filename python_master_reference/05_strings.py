"""
05 - Strings
String means text.
"""

first_name = "Khadir"

last_name = "Zavareh"

full_name = first_name + " " + last_name  # Join strings together

print(full_name)

message = f"My name is {first_name}."  # f-string puts variables inside text

print(message)

sentence = "Python is useful for test automation."

print(sentence.upper())  # Uppercase

print(sentence.lower())  # Lowercase

print(sentence.replace("Python", "Robot Framework"))  # Replace text

print(len(sentence))  # Count characters

print(sentence[5])  # First character

print(sentence[0:6])  # Characters from index 0 to 5
