import time, random

print("Welcome To The personality Quiz!")

score = 0

print(""" When you meet someone for the first time:
a. you talk more
b. they talk more
""")
answer_1 = input()

if answer_1 == "a":
  score += 1 
else:
    score -= 1

print("""do you thalk or read more
a. you read more
b. you talk more""")
answer_2 = input()

if answer_2 == "a":
      score -= 1
else:
        score += 1

print (""" Would you rather
a. Play with your friends
b. Play alone""")
answer_3 = input()

if answer_3 == "a":
  score += 1

else:
        score -= 1

print ("Processing Results")

for i in range (20000):
  print(random.randint(0,1),end="",flush=True)

  if score > 1:
    print("youre really introvered")
  elif score<=2 and score>=0:
    print("you're somewhere in the middle")
  else:
    print("you're really extroverted")