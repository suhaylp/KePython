# Global variable for username
username = ""

def start_game():
    global username
    print("Welcome to your very own interactive Paw Patrol Adventure Bay game.")
    username = input("Enter your name: ")
    place_chooser()


def place_chooser():
    choice = input(f"Hi {username}, choose where you would like to explore: Barkingburg, Foggy Bottom, or Katies Pet Parlor: ").lower()
    if choice == "barkingburg":
        barkingburg()
    elif choice == "foggy bottom":
        foggybottom()
    elif choice == "katies pet parlor":
        katies_pet_parlor()
    else:
        print("That isn't an option. Please pick from the three choices listed above.")
        place_chooser()


def katies_pet_parlor():
    print("Welcome to Katie's Pet Parlor! I am Ryder and I have chosen you to help me with this mission.\n"
          "Katie's cat has climbed onto the roof, and Skye isn't able to get her down.\n"
          "She says we have to answer 3 riddles of hers and then she will agree to coming down.\n"
          "For each question you have three tries to answer.\n"
          "We need your quick thinking on this mission. Please hurry!")
    katies_q1(3)


def katies_q1(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q1 = input("10 copycats were sitting in a car. One jumped out. How many are left? ").lower()
    if "zero" in q1 or "0" in q1 or "none" in q1:
        print("Hissssss, you got this question right, here is the next question: ")
        katies_q2(attempts)
    else:
        print(f"Wrong! You only have {attempts - 1} more attempt(s) on this question!")
        katies_q1(attempts - 1)


def katies_q2(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q2 = input("I'm found in socks, scarves, and mittens. I'm found in the paws of playful kittens. What am I? ").lower()
    if "yarn" in q2 or "wool" in q2:
        print("Oh no, you got it right again! I'm not coming down. Don't get this next one right!")
        katies_q3(attempts)
    else:
        print(f"Wrong! You only have {attempts - 1} more attempt(s) on this question!")
        katies_q2(attempts - 1)


def katies_q3(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q3 = input("How many lives does a cat have? ").lower()
    if "nine" in q3 or "9" in q3 or "nine lives" in q3 or "nine lifes" in q3 or "9 lives" in q3:
        print(f"I am a cat of my word, sadly I will have to come down. Good job, I now declare you to be an honorary member of the Paw Patrol, {username}!")
        print("You have completed your mission.")
    else:
        print(f"Wrong! You only have {attempts - 1} more attempt(s) on this question!")
        katies_q3(attempts - 1)



def barkingburg():
    print("Welcome to barkingburg, isn't it just stunning. Sadly, we aren't here for a pleasant trip, we are here for a mission. I ryder have chosen you because of your impressive skill sets, and your smarts. Someone has stolen the princesses tiara! It is your duty to find it for the princess. SHe is depending on you. This may seem like a daunting quest, but don't worry, we know where the crown is. This is because it has a secret location tracker hidden in one of the diamonds. THe tracker shows that she is in the vault room, which is an enclosed room. ")
    print ("The bad news is that the vault room is locked, and to open it you hae to answer three very difficult riddles. You only have 3 tries per question, use them wisely. Once you do that the room will open.")
    barkingburg_q1(3)

#TODO complete barkingburg, questions, and wirte an ending message, and finish some of the story line, for guidance look at the document you made. 

def barkingburg_q1(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q1 = input("ENTER QUESTION HERE").lower()
    if "" in q1 or "x" in q1 or "x" in q1 or "x" in q1:
        print("Wow! You got this question right, here is the next question: ")
        barkingburg_q2(attempts)
    else:
        print(f"Sorry, you got that wrong! You only have {attempts - 1} more attempt(s) on this question!")
        barkingburg_q1(attempts - 1)


def barkingburg_q2(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q2 = input("ENTER QUESTION HERE").lower()
    if "x" in q2 or "x" in q2:
        print ("Awesome, you got it right again!")
        barkingburg_q3(attempts)
    else:
        print(f"Good try, you only have {attempts - 1} more attempt(s) on this question!")
        barkingburg_q2(attempts - 1)


def barkingburg_q3(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q3 = input("ENTER QUESTION HERE").lower()
    if "x" in q3 or "x" in q3 or "x" in q3:
        print(f"x") 
    else:
        print(f"Wrong! You only have {attempts - 1} more attempt(s) on this question!")
        barkingburg_q3(attempts - 1)



def foggybottom():
    print(
        "Welcome to Foggy Bottom. Mayor Humdinger wants to take over Adventure Bay, "
          "and what you need to do to stop him is to prevent his boat from picking him up so he can't cross into Adventure Bay."
          "\nYou see Wally in the sea, and since Wally's owner is Cap'n Turbot who is steering the ship, he can tell him to stop the boats. "
          "\n Wa;;y says he will only complete your request if you get im 3 squid peices. You run to the nearest fish market to get Wally his treats but you realize you don't have any money on you."
          "\nSince the shop owner is kind, he offers to give you the squid if you answer 3 riddles with 3 tries for each riddle."
          "\nIf you get them correct, he will give you the squid!")
    foggy_q1(3)


def foggy_q1(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q1 = input("How do you make an octopus laugh?").lower()
    if "10" in q1 or "ten" in q1 or "tickles" in q1 or "tenticles" in q1:
        print("Wow! You got this question right, here is the next question: ")
        foggy_q2(attempts)
    else:
        print(f"Sorry, you got that wrong! You only have {attempts - 1} more attempt(s) on this question!")
        foggy_q1(attempts - 1)

def foggy_q2(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q2 = input("What has hands buut can't clap?").lower()
    if "clock" in q2 or "watch" in q2:
        print ("You got it right again!")
        foggy_q3(attempts)
    else:
        print(f"Wrong! You only have {attempts - 1} more attempt(s) on this question!")
        foggy_q2(attempts - 1)


def foggy_q3(attempts):
    if attempts == 0:
        print("You've run out of attempts! Let's try a different mission.")
        place_chooser()
        return
    q3 = input("What has keys, but can't open any doors? ").lower()
    if "piano" in q3 or "keyboard" in q3 or "grand" in q3:
        print(f"That's impressive! I really didn't think you would get. Here is the octopus leg. Go give it Wally quickly!") 
        print("You run tp give it wally, and he happily eats it, and swims to captain turbot.\n You wonder how you will know if wally tells captain turbot to turn the boat around, but then you see the boat turn around, and cruise of away from fogg bottom.")
        print("Ryder comes up to you and tells you, 'Good job, You have completed your mission we are all very proud of you. We know delcare you an honorary member of the paw patrol.' ")
    else:
        print(f"Wrong! You only have {attempts - 1} more attempt(s) on this question!")
        foggy_q3(attempts - 1)


start_game()
