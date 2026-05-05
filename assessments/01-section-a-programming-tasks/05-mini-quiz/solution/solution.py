score = 0

answer1 = input("What is 5 + 7? ")
if answer1 == "12":
    score = score + 1

answer2 = input("What is the capital of France? ")
if answer2 == "Paris":
    score = score + 1

answer3 = input("What colour do you get when you mix red and blue? ")
if answer3.lower().strip() == "purple":
    score = score + 1

print(f"You scored {score} out of 3")
