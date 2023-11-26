import time
import random
import keyboard
import math
import shelve


first_time = True

def user():
    print("=" * 50)
    intro = print("Welcome to the speed typing test")
    global username
    with shelve.open("users.db") as db:
        
        username = input("What is your username: ").strip().capitalize()
            
        if username not in db:
            print("Your new around here welcome {}.".format(username))
            db[username] = True
        else:
            first_time = False
            print("Welcome back {}".format(username))


def average_answers():
    global username
    global first_time
    
    if first_time == True:
        try:  
            with open(username, "r") as file:
                existing_data = file.read()
        except FileNotFoundError:
                existing_data = ""

        with open(username, "a") as file:
            new_data = str(int(rounded_percentage))
            file.write(new_data + "\n")
            all_data = existing_data + new_data
            pass
    else:
        pass
    
    myFile = open(username, "r")

    lines = []

    for line in myFile:
        lines.append(line.strip())

    integer_lines = [int(line) for line in lines if line.strip()]
    total_sum = sum(integer_lines)

    average = total_sum / len(lines)
    print("Your average of correct answers is {}%".format(int(average)))


def average_speed():
    global username
    
    if first_time == True:
        try:  
            with open(username + "speed", "r") as file:
                existing_data = file.read()
        except FileNotFoundError:
                existing_data = ""

        with open(username + "speed", "a") as file:
            new_data = str(int(rounded_time))
            file.write(new_data + "\n")
            all_data = existing_data + new_data
            pass
    else:
        pass
    
    myFile = open(username + "speed", "r")

    lines = []

    for line in myFile:
        lines.append(line.strip())

    float_lines = [float(line) for line in lines if line.strip()]
    total_sum = sum(float_lines)

    average = total_sum / len(lines)
    print("Your average speed is {} seconds".format(int(average)))
            
     
user()

print("Game starting in 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# list of possible sentences
sentences = [
    "The sun rises in the east and sets in the west.",
    "Elephants are the largest land animals on Earth.",
    "Apples are a popular fruit and come in various colors.",
    "Mount Everest is the highest peak in the world.",
    "The Mona Lisa is a famous painting by Leonardo da Vinci.",
    "The Great Wall of China is visible from space.",
    "Bees play a vital role in pollination and ecosystem health.",
    "The Pacific Ocean is the largest ocean on the planet.",
    "The human brain weighs about 3 pounds and controls our thoughts.",
    "Giraffes have long necks that help them reach leaves in tall trees.",
    "The Eiffel Tower is a symbol of Paris and France.",
    "Water boils at 100 degrees Celsius (212 degrees Fahrenheit).",
    "The Sahara Desert is the largest hot desert in the world.",
    "Honey is produced by bees using nectar from flowers.",
    "The Amazon Rainforest is home to a diverse range of species.",
    "The moon orbits around the Earth and causes tides.",
    "The Statue of Liberty was a gift from France to the United States.",
    "Penguins are flightless birds that inhabit the Southern Hemisphere.",
    "The Nile River is the longest river in the world.",
    "Diamonds are formed deep within the Earth's mantle.",
    "The moonlit night was filled with tranquility.",
    "Coding challenges help improve problem-solving skills.",
    "Whales are magnificent creatures of the ocean.",
    "Cooking can be both an art and a science.",
    "The Pyramids of Giza are ancient wonders of the world.",
    "The sound of waves crashing is soothing to many.",
    "Exploring space raises fundamental questions about existence.",
    "Education is a lifelong journey.",
    "Sunsets paint the sky in beautiful colors.",
    "Yoga and meditation promote mental and physical well-being.",
    "Writing is a powerful form of self-expression.",
    "Rainforests host incredible biodiversity.",
    "Traveling exposes you to different cultures and perspectives.",
    "Physics explains the fundamental laws of the universe.",
    "Gardening is a therapeutic hobby for many.",
    "Challenges often lead to personal growth.",
    "Social media has reshaped how we connect with others.",
    "The energy from the sun sustains life on Earth.",
    "Archaeology uncovers stories of ancient civilizations.",
    "Empathy is the cornerstone of understanding.",
]


# print random sentence
random_sentence = random.choices(sentences)
typing = print( *random_sentence)
start = time.time()
result  = input(": ").strip()

if keyboard.is_pressed("enter"):
    pass
end = time.time()

# print results
new_time = end - start
# round to 2 decimal
rounded_time = round(new_time, 2)
print("Results:")
print("You took {:.2f} seconds".format(rounded_time))

list1 = list(*random_sentence)
list2 = list(result)

incorrect = 0
list3 = []

for i in range(len(list2)):
    if i < len(list1) and list2[i] != list1[i]:
        incorrect += 1
        list3.append(list2[i])
                
orig = len(list2) - len(list1)  
write = len(list1) - len(list2)
nolist = len(list3)

total_diff  = orig + write

if orig > 0:
    nolist += total_diff
elif write > 0:
    nolist += write
else:
    pass

print("You have gotten {} wrong letters".format(nolist))
correct = len(list1) - nolist

percentage = correct * 100 / len(list1)

rounded_percentage = round(percentage, 0)
print("You have scored {}% of correct answers".format(int(rounded_percentage)))


print("")
print("Averages of all your games:")
average_speed()
average_answers()

new_percentage = int(rounded_percentage)

if new_percentage >= 75 and rounded_time <= 20:
    print("Wow you are doing really well")
elif new_percentage <= 50:
    print("I´m sure you can do better next time")
elif new_percentage > 50 and new_percentage < 75:
    print("Well done")
elif new_percentage == 100:
    print("Perfect score!!!")

time.sleep(10)

print("")
print("What would you like to do?")
print("Reset scores [1]")
print("Exit [2]")
question = input(": ").strip()

if question == "1":
    with open(username, "w") as file:
        file.write("")
    with open(username + "speed", "w") as file:
        file.write("")
    print("Scores reset for user: {}".format(username))
    exit()
elif question == "2":
    print("Ok, goodbye!")
    time.sleep(1)
    exit()
else:
    print("Invalid choice.")


print("=" * 50)
