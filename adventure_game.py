import time
import random


def print_pause(print_msg):
    print(print_msg)
    time.sleep(1.2)


villians = ['Dragon', 'Evil Wizard', 'Giant', 'Griffin', 'Chimera']
villain = random.choice(villians)

items = ['dagger']  # what the main character is carrying


# input validation
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.\n")
    return response


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + villain +
                " is somewhere around here,"
                " and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " but not very effective dagger \n")


def play_again():
    response = valid_input("Would you like to play again?\n"
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("Ok. Thanks for playing.\n GOODBYE!")
    elif "yes" in response:
        print_pause("Wonderful. Adventure Awaits!")
        print_pause("Game restarting .... \n\n")
        if "sword" in items:
            items.remove("sword")
            items.append("dagger")
            play_game()
        else:
            play_game()


def choice_location():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    response = valid_input("What would you like to do?\n"
                           "Please enter 1 or 2.\n", "1", "2")
    if '1' in response:
        house()
    elif '2' in response:
        cave()


def runaway():
    print_pause("You run back into the field.\n"
                "Luckily, you don't seem to have been followed.\n")
    choice_location()


def fight():
    if 'sword' in items:
        print_pause("As the " + villain + " moves to attack,"
                                          " you unsheath your new sword")
        print_pause("The Sword of Lilith shines brightly "
                    "in your hand as you brace yourself for the attack")
        print_pause("But the " + villain + " takes one "
                                           "look at your shiny new toy and runs away")
        print_pause("You have rid the town of the " + villain)
        print_pause("You are victorious!")
        print_pause("GAME OVER!\n")
        play_again()
    elif 'dagger' in items:  # lose
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + villain)
        print_pause("You have been defeated\n")
        play_again()


def choice_action():  # fight or runaway
    response = valid_input("Would you like to (1) fight or (2) run away?\n",
                           "1", "2")
    if '1' in response:
        fight()
    elif '2' in response:
        runaway()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and"
                " out steps a " + villain)
    print_pause("OH NO! This is the " + villain + " house!")
    print_pause("The " + villain + " attacks you!")
    if "dagger" in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger\n")
        choice_action()
    #   elif "sword" in items:
    #        choice_action()
    else:
        choice_action()


def cave():
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        choice_location()
    else:
        print_pause("It turns out to be only a very small cave")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Lilith!")
        items.append('sword')
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        items.remove("dagger")
        print_pause("You walk back out to the field \n")
        choice_location()


def play_game():
    intro()
    choice_location()


play_game()
