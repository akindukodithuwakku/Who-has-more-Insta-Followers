import random
import os
from game_data import data

def max_num(compareA, compareB):
    A = compareA.get("follower_count")
    B = compareB.get("follower_count")

    if A > B:
        return 'A'
    else:
        return 'B'

score = 0
user_choice = None

while True:
    compareA = random.choice(data)
    compareB = random.choice(data)

    if compareA == compareB:
        # To avoid comparing the same items, continue to the next iteration.
        continue

    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}.")
    print(f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}.")

    user_choice = input("Who has more followers: 'A' or 'B'? ").lower()

    if user_choice == max_num(compareA, compareB).lower():
        score += 1
        print(f"You are right! Your current score is: {score}")
       
    else:
        print(f"Sorry, you made the wrong choice. Your final score is: {score}")
        break

