"""
13 - Dictionaries
Dictionary stores data as key-value pairs.
A list can store multiple dictionaries.
This is useful when we have more than one user.
"""

users = [
    {
        "name": "Khadir",
        "role": "QA Engineer",
        "city": "Helsinki"
    },
    {
        "name": "Jaakko",
        "role": "CEO",
        "city": "Turku"
    }
]

print(users)  # Print the full list of users


# Access the first user
print(users[0]["name"])  # Khadir
print(users[0]["role"])  # QA Engineer
print(users[0]["city"])  # Helsinki


# Access the second user
print(users[1]["name"])  # Jaakko
print(users[1]["role"])  # CEO
print(users[1]["city"])  # Turku


# Loop through all users
for user in users:
    print("-----")
    print(user["name"])
    print(user["role"])
    print(user["city"])


# Add a new key-value pair to the first user
users[0]["company"] = "JT Testing"

print(users[0])


# Update the city of the second user
users[1]["city"] = "Tampere"

print(users[1])


# Delete the city from the first user
del users[0]["city"]

print(users[0])