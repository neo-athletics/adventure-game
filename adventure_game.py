import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def field(villain):
    print_pause("You find yourself standing in an open field, \
filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around here, and \
has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) \
dagger.")


def cave_or_house():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


def prompt_cave_house():
    # keeps asking for input if not given correctly
    choice = input("(Please enter 1 or 2).\n")

    if choice == "1" or choice == "2":
        return choice
    else:
        return prompt_cave_house()


def house(villain, weapon):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens \
and out steps a {villain}.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} attacks you!")
    if weapon[-1] == "dagger":
        print_pause("You feel a bit under-prepared for this, what with only \
having a tiny dagger.")


def fight_or_flight():
    ready_or_not = input("Would you like to (1) fight or (2) run away?\n")
    if ready_or_not == "1" or ready_or_not == "2":
        return ready_or_not
    else:
        return fight_or_flight()


def found_new_weapon(weapon, new_weapons):
    weapon.append(random.choice(new_weapons))
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause(f"You have found the magical {weapon[-1]} of Ogoroth!")
    print_pause(f"You discard your silly old dagger and take \
the {weapon[-1]} with you.")
    print_pause("You walk back out to the field.")


def no_new_weapon():
    # going back into the cave after you have gone once
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff. \
It's just an empty cave now.")
    print_pause("You walk back out to the field.")


def cave(weapon, new_weapons):
    if weapon[-1] in new_weapons:
        no_new_weapon()
    else:
        found_new_weapon(weapon, new_weapons)


def restart_prompt():
    play_again = input("Would you like to play again? (y/n)\n")

    if play_again == "y" or play_again == "n":
        return play_again
    else:
        return restart_prompt()


def restart():
    play_again = restart_prompt()

    if play_again == "y":
        # play again restart game
        print_pause("Excellent! Restarting the game ...")
        start_journey()
    else:
        # end game
        print_pause("Thanks for playing! See you next time.")


def loose_fight(villain):
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {villain}.")
    print_pause("You have been defeated!")
    restart()


def win_fight(weapon, villain):
    print_pause(f"As the {villain} moves to attack, you unsheath \
your new {weapon[-1]}.")
    print_pause(f"The {weapon[-1]} of Ogoroth shines brightly in your hand as \
you brace yourself for the attack.")
    print_pause(f"But the {villain} takes one look at your shiny new toy \
and runs away!")
    print_pause(f"You have rid the town of the {villain}. You are victorious!")
    restart()


def fight(weapon, new_weapons, villain):
    if weapon[-1] not in new_weapons:
        # you fight without a new weapon
        loose_fight(villain)
    else:
        # fight with new weapon
        win_fight(weapon, villain)


def life_or_death(weapon, villain, new_weapons):

    stranger_danger = prompt_cave_house()

    if stranger_danger == "1":
        house(villain, weapon)
        foe_or_fly = fight_or_flight()

        if foe_or_fly == "1":
            # start fight
            fight(weapon, new_weapons, villain)

        elif foe_or_fly == "2":
            # back to field
            print_pause("You run back into the field. Luckily, you don't \
seem to have been followed.")
            return on_field(weapon, villain, new_weapons)

    elif stranger_danger == "2":
        # head to cave
        cave(weapon, new_weapons)
        on_field(weapon, villain, new_weapons)


def on_field(weapon, villain, new_weapons):
    cave_or_house()
    life_or_death(weapon, villain, new_weapons)


def start_journey():
    weapon = ["dagger"]
    villain = random.choice(["pirate", "wicked fairie", "bearpig",
                            "ancient turtle"])
    new_weapons = ["sword", "blades", "shield", "bow and arrow"]
    field(villain)
    on_field(weapon, villain, new_weapons)


if __name__ == "__main__":
    # setup game
    start_journey()
    pass
