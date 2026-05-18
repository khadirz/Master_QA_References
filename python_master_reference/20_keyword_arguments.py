"""
20 - Keyword Arguments
Keyword arguments make function calls easier to read.
"""

def create_user(name, role, city):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"City: {city}")

create_user(name="Khadir", role="Tester", city="Helsinki")
create_user(city="Turku", name="Jaakko", role="CEO")  # Order does not matter with keyword arguments

