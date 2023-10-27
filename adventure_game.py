import time
import random

def print_with_sleep(text, sleep_time=2):
    print(text)
    time.sleep(sleep_time)

def empty_cave_message():
    print_with_sleep("You've been here before and gotten all the good stuff.")
    print_with_sleep("It's just an empty cave now.")
    print_with_sleep("You walk back out to the field")

def encounter_enemy(enemy):
    found_sword = False  # Variable to track if the player found the sword
    
    while True:
        response = input("Enter 1 to knock on the door of the house, Enter 2 to go to the cave instead: ")

        if response == "1":
            # Handle the door of the house
            if not found_sword:  # Check if the player found the sword
                print_with_sleep("You approach the door of the house.")
                print_with_sleep(f"As you knock, the door opens, and out steps a {enemy}")
                print_with_sleep("Eep! This is not what you expected!")
                print_with_sleep(f"The {enemy} attacks you")
                print_with_sleep("You feel a bit under-prepared for this, what with only having a tiny dagger")
                fight_or_run = input("Would you like to (1) fight or (2) run away? ")
                if fight_or_run == "1":
                    print_with_sleep("You try your best...")
                    print_with_sleep(f"You bravely fight the {enemy} but unfortunately meet your end")
                    print_with_sleep("You are defeated...")
                    break  # Exit the encounter loop
                else:
                    print_with_sleep("You manage to escape.")
                    print_with_sleep("Luckily, you don't seem to have been followed.")
                    print_with_sleep("Please enter 1 or 2")
                    response = input("Enter 1 to go back to the field, Enter 2 to peer into the cave: ")
                    if response == "1":
                         encounter_enemy(enemy)# Exit the loop and go back to the field
                    elif response =="2":
                         print_with_sleep("You decided to check out the dark cave with bravery.")
                
            else:
                # Handle the player having the sword
                print_with_sleep("You approach the door of the house.")
                print_with_sleep(f"As you knock, the door opens, and out steps a {enemy}")
                print_with_sleep("Eep! It looked scarier that your first encounter!")
                print_with_sleep(f"The {enemy} attacks you")
                print_with_sleep(f"As the {enemy} moves to attack, you unsheathe your new sword.")
                print_with_sleep("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
                print_with_sleep(f"But the {enemy} takes one look at your shiny new toy and runs away!")
                print_with_sleep(f"You have rid the town of the {enemy}. You are victorious!")
                playgameagain()
                continue
        elif response == "2":
            # Handle the cave
            if not found_sword:  # Check if the player found the sword
                print_with_sleep("You peer cautiously into the cave")
                print_with_sleep("It turns out to be only a very small cave")
                print_with_sleep("Your eye catches a glint of metal behind a rock")
                print_with_sleep("You have found the magical Sword of Ogoroth!")
                print_with_sleep("You discard your silly old dagger and take the sword with you")
                print_with_sleep("You walk back to the field")
                found_sword = True  # Mark that the player found the sword
            else:
                while True:
                    print_with_sleep("Please enter 1 or 2")
                    response = input("Enter 1 to go back to the field, Enter 2 to peer into the cave: ")
                    if response == "1":
                       break  # Exit the loop and go back to the field
                    elif response =="2":
                         empty_cave_message()
                    else:
                         print_with_sleep("Please enter 1 or 2")
            continue             
        else:
            print_with_sleep("Please enter 1 or 2")

def main():
    while True:
        enemies = ["Devil Fairy", "Bad Pirates", "Big Dragon", "Troll"]
        enemy = random.choice(enemies)
        print_with_sleep("You find yourself standing in an open field, filled with grass and yellow wildflowers")
        print_with_sleep(f"Rumor has it that a {enemy} is somewhere around here and has been terrorizing the nearby village")
        print_with_sleep("In front of you is a house")
        print_with_sleep("To your right is a dark cave")
        print_with_sleep("In your hand, you hold your trusty (but not very effective) dagger")
        encounter_enemy(enemy)
        if not playgameagain():
            break

def playgameagain():
    while True:
        play_again = input("Would you like to play another game? (y/n): ").lower()
        if play_again == 'n':
            print_with_sleep("OK, Goodbye!")
            return False
        elif play_again == 'y':
            print_with_sleep("Very good, let's restart the game!")
            return main

if __name__ == "__main__":
    main()
