import random

def random_choice_number(low, high):
    return random.choice(range(low, high))

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: ")) + 1

print(random_choice_number(low, high))