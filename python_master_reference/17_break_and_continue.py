"""
17 - Break and Continue
break stops a loop.
continue skips the current round.
"""

for number in range(10):
    if number == 5:
        break
    print(number) #prints 0 to 4

print("Second loop")

for number in range(5):
    if number == 2:
        continue
    print(number) #prints 0, 1, 3, 4 (skips 2)
