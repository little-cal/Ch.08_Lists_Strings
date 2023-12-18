'''
ADVENTURE GAME (4pts)
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random

# user input options
ghost_question = "Where are you?, Are you here?, Are you friendly?, How old are you?"
user_actions = "Check temperatures, Look for EMF readings, Talk to the ghost, Taunt the Ghost, " \
               "Set up a salt barrier, Attempt an exorcism, Move to different room, Quit"
# set of rooms for the house, numbered for clarity
room_list = []
room0 = ["\033[1;32m" + 'You are on the Porch.' + "\033[0m", 1, None, None, None]
room_list.append(room0)
room1 = ["\033[1;32m" + 'You are in the Living Room.' + "\033[0m", 2, None, None, None]
room_list.append(room1)
room2 = ["\033[1;32m" + 'You are in the Kitchen.' + "\033[0m", 4, None, 1, 3]
room_list.append(room2)
room3 = ["\033[1;32m" + 'You are in the Garage.' + "\033[0m", None, 2, None, None]
room_list.append(room3)
room4 = ["\033[1;32m" + 'You are in the South Hallway.' + "\033[0m", 6, 5, 2, 9]
room_list.append(room4)
room5 = ["\033[1;32m" + 'You are in the Bathroom.' + "\033[0m", None, None, None, 4]
room_list.append(room5)
room6 = ["\033[1;32m" + 'You are in the North Hallway.' + "\033[0m", None, 7, 4, 8]
room_list.append(room6)
room7 = ["\033[1;32m" + 'You are in the Small Bedroom.' + "\033[0m", None, None, None, 6]
room_list.append(room7)
room8 = ["\033[1;32m" + 'You are in the Large Bedroom.' + "\033[0m", 7, 6, None, None]
room_list.append(room8)
room9 = ["\033[1;32m" + 'You are on the Basement Stairs' + "\033[0m", None, 4, None, 10]
room_list.append(room9)
room10 = ["\033[1;32m" + 'You are in the North Basement Hallway.' + "\033[0m", None, 9, 11, None]
room_list.append(room10)
room11 = ["\033[1;32m" + 'You are in the South Basement Hallway.' + "\033[0m", 10, 13, 12, None]
room_list.append(room11)
room12 = ["\033[1;32m" + 'You are in the Small Storage Room.' + "\033[0m", 11, None, None, None]
room_list.append(room12)
room13 = ["\033[1;32m" + 'You are in the East Basement Hallway' + "\033[0m", None, None, 14, 11]
room_list.append(room13)
room14 = ["\033[1;32m" + 'You are in the Large Storage Room.' + "\033[0m", 13, None, None, None]
room_list.append(room14)

# current room value and booleans
current_room = 0
done = False
exorcism_capable = False
player_kill = False


# functions to call during the outcome of an exorcism
def win():
    print("\n\033[0;36m" + 'Congratulations on beating my game! I hope you had fun!' + "\033[0m")


def lose():
    print("\n\033[0;36m" + 'Thanks for playing my game!' + "\033[0m")


# function for the different actions the ghost can do
def ghost_action():
    # basing the selection of actions based off the ghost's activity level and a random integer
    # odds for an action to occur increase as the ghost's activity level increases
    if ghost.activity_level == 1:
        action = random.randint(1, 20)
        if action == 1:
            print("The Ghost threw a small picture frame across the room.")
        elif action == 2:
            print("A door near you creaks closed.")
        elif action == 3:
            print("A door near you slammed shut.")
        elif action == 4:
            print("A loud bang startles you as the Ghost knocks on the wall.")
        else:
            pass
    elif ghost.activity_level == 2:
        action = random.randint(1, 15)
        if action == 1:
            print("The Ghost threw a small picture frame across the room.")
        elif action == 2:
            print("A door near you creaks closed.")
        elif action == 3:
            print("A door near you slammed shut.")
        elif action == 4:
            print("A loud bang startles you as the Ghost knocks on the wall.")
        else:
            pass
    else:
        action = random.randint(1, 10)
        if action == 1:
            print("The Ghost threw a small picture frame across the room.")
        elif action == 2:
            print("A door near you creaks closed.")
        elif action == 3:
            print("A door near you slammed shut.")
        elif action == 4:
            print("A loud bang startles you as the Ghost knocks on the wall.")
        else:
            pass


# function that runs through the exorcism of the ghost
def exorcism():
    # check for too high of ghost anger, ends the game
    if player_kill:
        print("\nThe ghost is too angry for an exorcism to work.")
        print("\nYou've made a grave mistake coming in here...")
        print("Your silly little exorcism will do nothing to me...")
        print("\033[1;31m" + 'NOW LEAVE!!!' + "\033[0m")
        lose()
    # on the easiest difficulty, exorcism works 100% of the time
    elif ghost.ghost_difficulty == 1:
        print("\nAs you start your incantation, the angry ghost writhes in pain.")
        print("Trapped and unable to escape, the ghost melts away.")
        print("The deathly aura surrounding the house seems to disappear.")
        win()
    # medium difficulty, 70% chance for the exorcism to work
    elif ghost.ghost_difficulty == 2:
        exorcism_chance = random.randint(0, 100)
        if exorcism_chance >= 30:
            print("\nAs you start your incantation, the angry ghost writhes in pain.")
            print("Trapped and unable to escape, the ghost melts away.")
            print("The deathly aura surrounding the house seems to disappear.")
            win()
        else:
            print("\nYou've made a grave mistake coming in here...")
            print("Your silly little exorcism will do nothing to me...")
            print("\033[1;31m" + 'NOW LEAVE!!!' + "\033[0m")
            lose()
    # hardest difficulty, 50% chance for the exorcism to work
    else:
        exorcism_chance = random.randint(0, 100)
        if exorcism_chance >= 50:
            print("\nAs you start your incantation, the angry ghost writhes in pain.")
            print("Trapped and unable to escape, the ghost melts away.")
            print("The deathly aura surrounding the house seems to disappear.")
            win()
        else:
            print("\nYou've made a grave mistake coming in here...")
            print("Your silly little exorcism will do nothing to me...")
            print("\033[1;31m" + 'NOW LEAVE!!!' + "\033[0m")
            lose()


# runs through all the different options for each different question
# different answers depending on the range to the ghost
def ghost_convo():
    # check for the player range to ghost location
    # if in range, able to ask a question
    # answers to questions change when you get closer
    # some change according to difficulty

    # first range check
    if action_range == 2:
        print("\n\033[1;34m" + 'What would you like to ask the ghost? (1-4)' + "\033[0m")
        ghost_query = int(input(ghost_question + "\n:"))
        if ghost_query == 1:
            question_chance = random.randint(1, 4)
            if question_chance == 1:
                print("\n\033[1;35m" + 'Far...' + "\033[0m")
            elif question_chance == 2:
                print("\n\033[1;35m" + 'Not here...' + "\033[0m")
            elif question_chance == 3:
                print("\n\033[1;35m" + 'Away...' + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 2:
            question_chance = random.randint(1, 3)
            if question_chance == 1:
                print("\n\033[1;35m" + 'Not here...' + "\033[0m")
            elif question_chance == 2:
                print("\n\033[1;35m" + 'No...' + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 3:
            if ghost.ghost_difficulty == 1:
                question_chance = random.randint(1, 3)
                if question_chance == 1:
                    print("\n\033[1;35m" + 'Maybe...' + "\033[0m")
                elif question_chance == 2:
                    print("\n\033[1;35m" + 'Are you?...' + "\033[0m")
                else:
                    print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
            else:
                question_chance = random.randint(1, 4)
                if question_chance == 1:
                    print("\n\033[1;35m" + 'Attack...' + "\033[0m")
                    ghost.anger += 1
                elif question_chance == 2:
                    print("\n\033[1;35m" + 'Get out...' + "\033[0m")
                    ghost.anger += 1
                elif question_chance == 3:
                    print("\n\033[1;35m" + 'Leave...' + "\033[0m")
                    ghost.anger += 1
                else:
                    print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        else:
            question_chance = random.randint(1, 2)
            if question_chance == 1:
                ghost.age = str(ghost.age) + '...'
                print("\n\033[1:35m" + ghost.age + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
# second range check
    elif action_range == 1:
        print("\n\033[1;34m" + 'What would you like to ask the ghost? (1-4)' + "\033[0m")
        ghost_query = int(input(ghost_question + "\n:"))
        if ghost_query == 1:
            question_chance = random.randint(1, 4)
            if question_chance == 1:
                print("\n\033[1;35m" + 'Close...' + "\033[0m")
            elif question_chance == 2:
                print("\n\033[1;35m" + 'Near...' + "\033[0m")
            elif question_chance == 3:
                print("\n\033[1;35m" + 'I can see you...' + "\033[0m")
                ghost.anger += 1
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 2:
            question_chance = random.randint(1, 3)
            if question_chance == 1:
                print("\n\033[1;35m" + 'Not here...' + "\033[0m")
            elif question_chance == 2:
                print("\n\033[1;35m" + 'No...' + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 3:
            if ghost.ghost_difficulty == 1:
                question_chance = random.randint(1, 3)
                if question_chance == 1:
                    print("\n\033[1;35m" + 'Maybe...' + "\033[0m")
                elif question_chance == 2:
                    print("\n\033[1;35m" + 'Are you...' + "\033[0m")
                else:
                    print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
            else:
                question_chance = random.randint(1, 4)
                if question_chance == 1:
                    print("\n\033[1;35m" + 'Attack...' + "\033[0m")
                    ghost.anger += 1
                elif question_chance == 2:
                    print("\n\033[1;35m" + 'Get out...' + "\033[0m")
                    ghost.anger += 1
                elif question_chance == 3:
                    print("\n\033[1;35m" + 'Leave...' + "\033[0m")
                    ghost.anger += 1
                else:
                    print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        else:
            question_chance = random.randint(1, 2)
            if question_chance == 1:
                ghost.age = str(ghost.age) + '...'
                print("\n\033[1:35m" + ghost.age + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
# third range check
    elif current_room == ghost.location:
        print("\n\033[1;34m" + 'What would you like to ask the ghost? (1-4)' + "\033[0m")
        ghost_query = int(input(ghost_question + "\n:"))
        if ghost_query == 1:
            question_chance = random.randint(1, 4)
            if question_chance == 1:
                print("\n\033[1;35m" + 'Here...' + "\033[0m")
            elif question_chance == 2:
                print("\n\033[1;35m" + 'Behind you...' + "\033[0m")
                ghost.anger += 1
            elif question_chance == 3:
                print("\n\033[1;35m" + 'Next to you...' + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 2:
            question_chance = random.randint(1, 3)
            if question_chance == 1:
                print("\n\033[1;35m" + 'I\'m here...' + "\033[0m")
            elif question_chance == 2:
                print("\n\033[1;35m" + 'Yes...' + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 3:
            if ghost.ghost_difficulty == 1:
                question_chance = random.randint(1, 3)
                if question_chance == 1:
                    print("\n\033[1;35m" + 'Maybe...' + "\033[0m")
                elif question_chance == 2:
                    print("\n\033[1;35m" + 'Are you?...' + "\033[0m")
                else:
                    print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
            else:
                question_chance = random.randint(1, 4)
                if question_chance == 1:
                    print("\n\033[1;35m" + 'Attack...' + "\033[0m")
                    ghost.anger += 1
                elif question_chance == 2:
                    print("\n\033[1;35m" + 'Get out...' + "\033[0m")
                    ghost.anger += 1
                elif question_chance == 3:
                    print("\n\033[1;35m" + 'Leave...' + "\033[0m")
                    ghost.anger += 1
                else:
                    print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
        elif ghost_query == 4:
            question_chance = random.randint(1, 2)
            if question_chance == 1:
                ghost.age = str(ghost.age) + '...'
                print("\n\033[1:35m" + ghost.age + "\033[0m")
            else:
                print("\n\033[0;36m" + 'You got no response.' + "\033[0m")
    else:
        print("\n\033[0;36m" + 'You are too far away to talk to the ghost.' + "\033[0m")


# creating ghost class, gives it different properties
class Ghost:

    def __init__(self, ghost_difficulty, location, activity_level, anger, age, trapped):
        self.ghost_difficulty = ghost_difficulty
        self.location = location
        self.activity_level = activity_level
        self.anger = anger
        self.age = age
        self.trapped = trapped


# instructions / info for the game
print("Welcome to my fun Ghost Game.")
print("The goal of this game is to find to navigate the house and locate the ghost.")
print("To find the ghost, you will be able to do certain actions within a room.")
print("\n\033[3m" + 'During action selection, type the number followed by info to see it\'s information.' + "\033[0m")
print("\nTo win this game, you will have to successfully exorcise the ghost.")
print("To begin, please select a difficulty (1-3)")
difficulty = input("Easy, Medium, Hard.\n:")
if difficulty.lower() == "easy" or difficulty == "1":
    difficulty = 1
elif difficulty.lower() == "medium" or difficulty == "2":
    difficulty = 2
elif difficulty.lower() == "hard" or difficulty == "3":
    difficulty = 3
else:
    print("\nThat is not an option, your difficulty will be randomized.")
    difficulty = random.randint(1, 3)

# creating the ghost
ghost = Ghost(difficulty, random.randint(1, 14), 1, 0, random.randint(50, 500), False)
# room 8 are the stairs, re-rolls location value
while ghost.location == 8:
    ghost.location = random.randint(1, 14)

# changes base anger depending on difficulty, default is zero
if ghost.ghost_difficulty == 2:
    ghost.anger = 10
elif ghost.ghost_difficulty == 3:
    ghost.anger = 20

# lets the player know where they start
print("\nApproaching the creaky old house, you step up onto the porch, sealing your fate.")

# main loop of the game
while not done:
    print("")
    # increases ghost.anger every iteration of the loop
    ghost.anger += 2
    # temp values of rooms
    ghost_room_temp = random.randint(10, 31)
    reg_room_temp = random.randint(32, 65)
    # dictates action range of ghost
    action_range = ghost.location - current_room

    # check for anger, increases activity level
    if ghost.anger == 30:
        ghost.activity_level = 2
    if ghost.anger == 70:
        ghost.activity_level = 3

    # asking for user input for direction

    user_choice = input("\033[0;36m" + 'What direction would you like to go? (N, E, S, W, Q for quit): ' + "\033[0m")

    # user movement logic
    if user_choice.lower() == "n" or user_choice.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("\n\033[1;31m" + 'You can\'t go that way' + "\033[0m")
            continue
        else:
            current_room = next_room
    elif user_choice.lower() == "e" or user_choice.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("\n\033[1;31m" + 'You can\'t go that way' + "\033[0m")
            continue
        else:
            current_room = next_room
    elif user_choice.lower() == "s" or user_choice.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("\n\033[1;31m" + 'You can\'t go that way' + "\033[0m")
            continue
        else:
            current_room = next_room
    elif user_choice.lower() == "w" or user_choice.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("\n\033[1;31m" + 'You can\'t go that way' + "\033[0m")
            continue
        else:
            current_room = next_room
    elif user_choice.lower() == "q" or user_choice.lower() == "quit":
        done = True
        continue
    else:
        print("\n\033[1;31m" + 'That is not an option.' + "\033[0m")
        continue

# loop for actions while in the same room
    while current_room == current_room:
        action_range = ghost.location - current_room
        ghost.anger += 1
# anger check, warning and exorcism capable check
        if ghost.anger >= 90:
            print("\n\033[1;31m" + 'The ghost is very angry.' + "\033[0m")
            exorcism_capable = True
# second anger check for killing the player
        if ghost.anger >= 100 and ghost.trapped is False:
            kill_chance = random.randint(1, 5)
            if kill_chance == 3:
                print("\nYou seem to have overstayed your welcome.")
                print("Without warning, a blurry figure darts across your vision.")
                print("Everything quickly fades to black.")
                lose()
                done = True
                break
# printing location of the player
        print("\n", room_list[current_room][0])
# calling ghost action function if in ghost room or in range
        if current_room == ghost.location:
            ghost_action()
        elif action_range < 3:
            ghost_action()
# user action while in a room
        print("\nAvailable actions are listed below.")
        print("\n", user_actions)
        action_choice = (input("Select an action with numbers 1-8: "))

# first option of choices, temperature check of a room
        if action_choice == "1":
            if current_room == ghost.location:
                print("\nYou fumble for your thermometer and check the temperature of the room.")
                print("It reads:", ghost_room_temp, "degrees Fahrenheit")
                ghost_action()
                continue
            else:
                print("\nYou pull out your thermometer and check the temperature of the room.")
                print("It reads:", reg_room_temp, "degrees Fahrenheit")
                continue

# second option of choices, emf check, based on range to the ghost room
        elif action_choice == "2":
            emf_read = 0
            if action_range == 3:
                emf_read = random.randint(0, 2)
                print("\nPulling out your EMF reader, you look for any activity.")
                print("It shows a reading of", emf_read)
            elif action_range == 2:
                emf_read = 3
                print("\nPulling out your EMF reader, you look for any activity.")
                print("It shows a reading of", emf_read)
            elif action_range == 1:
                emf_read = random.randint(4, 5)
                print("\nPulling out your EMF reader, you look for any activity.")
                print("It shows a reading of", emf_read)
            elif current_room == ghost.location:
                emf_read = 5
                print("\nPulling out your EMF reader, you look for any activity.")
                print("It shows a reading of", emf_read)
            else:
                emf_read = 0
                print("\nPulling out your EMF reader, you look for any activity.")
                print("It shows a reading of", emf_read)

# third option, calls the conversation function
        elif action_choice == "3":
            ghost_convo()

# fourth option, random taunts of the ghost, increases anger
        elif action_choice == "4":
            taunt_num = random.randint(1, 5)
            if taunt_num == 1:
                print("\nYou make fun of the ghost's shabby house.")
                print("It becomes a little more angry")
                ghost.anger += 5
            elif taunt_num == 2:
                print("\nYou make fun of the ghost for being so old.")
                print("It becomes a little more angry")
                ghost.anger += 5
            elif taunt_num == 3:
                print("\nYou decide to mock the ghost.")
                print("Ghost's have feelings too. It becomes more angry")
                ghost.anger += 10
            elif taunt_num == 4:
                print("\nYou pinch your nose as you tell the ghost to take a shower.")
                print("It becomes more angry.")
                ghost.anger += 10
            else:
                print("\nYou couldn't think of anything to say.")

# fifth option, 'traps' ghost it its own room
# needs to be trapped for exorcism
        elif action_choice == "5":
            if current_room == ghost.location:
                print("\nYou decide to set up a salt barrier in this room.")
                print("The ghost is now trapped.")
                ghost.trapped = True
            else:
                print("\nThere is no point in placing a barrier here.")

# sixth option exorcism, only allows if there is sufficient anger, trapped?, and in the ghost room
        elif action_choice == "6":
            if exorcism_capable and current_room == ghost.location:
                # if ghost is too angry upon starting an exorcism, the game ends
                if ghost.anger >= 110:
                    player_kill = True
                    exorcism()
                    done = True
                    break
                else:
                    exorcism()
                    done = True
                    break
            else:
                print("\nYou cannot perform an exorcism at this time.")

# seventh option, breaks out of loop, goes back to direction choosing
        elif action_choice == "7":
            break
# secondary quit option, one in direction loop, one in action loop
        elif action_choice == "8":
            lose()
            done = True
            break
# lets the user see info about each option
        elif action_choice.lower() == "1 info":
            print("\n\033[0;33m" + 'Use the thermometer to check the temperature of a room.' + "\033[0m")
            print("\033[0;33m" + 'Anything below freezing(Fahrenheit)shows the location of the ghost.' + "\033[0m")
        elif action_choice.lower() == "2 info":
            print("\n\033[0;33m" + 'The emf reader essentially shows how close you are to the ghost.' + "\033[0m")
            print("\033[0;33m" + 'Higher numbers means you are closer.' + "\033[0m")
        elif action_choice.lower() == "3 info":
            print("\n\033[0;33m" + 'Use this to talk to the ghost and ask it questions.' + "\033[0m")
            print("\033[0;33m" + 'If you are out of range, you won\'t be able to talk to the ghost.' + "\033[0m")
        elif action_choice.lower() == "4 info":
            print("\n\033[0;33m" + 'Use this to taunt the ghost. Taunting the ghost will make it angry.' + "\033[0m")
            print("\033[0;33m" + 'If the ghost is angry enough, you will be able to exorcise it.' + "\033[0m")
        elif action_choice.lower() == "5 info":
            print("\n\033[0;33m" + 'This will set up a salt barrier, trapping the ghost.' + "\033[0m")
            print("\033[0;33m" + 'Make sure the ghost is trapped before you exorcise it.' + "\033[0m")
        elif action_choice.lower() == "6 info":
            print("\n\033[0;33m" + 'If requirements are met, you will be able to exorcise the ghost.' + "\033[0m")
            print("\033[0;33m" + 'Be careful. If the ghost is too angry, you won\'t be able to exorcise it.' + "\033[0m")
        elif action_choice.lower() == "7 info":
            print("\n\033[0;33m" + 'Use this to select the next room you would like to move to.' + "\033[0m")
        elif action_choice.lower() == "8 info":
            print("\n\033[0;33m" + 'Quits the game.' + "\033[0m")
# any other input restarts the loop
        else:
            print("\nThat isn't an option.")
            continue
