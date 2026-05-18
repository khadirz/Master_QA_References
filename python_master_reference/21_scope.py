"""
21 - Scope
Scope means where a variable can be used.
"""

global_name = "Khadir"  # Global variable

def show_name():
    local_message = "Hello"  # Local variable
    print(local_message, global_name)

show_name()

# print(local_message)  # This would cause an error because it is local
