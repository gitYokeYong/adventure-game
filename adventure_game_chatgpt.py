import time
import random

enemies = ["Devil Fairy", "Bad Pirates", "Big Dragon"]

def print_with_sleep(text, sleep_time=2):
    print(text)
    time.sleep(sleep_time)

def encounter_enemy():
    # Function to handle an enemy encounter
    while True:
        response = input("Enter 1 to knock on the door of the house, Enter 2 to peer into the cave: ")

        if response == "1":
            enemy = random.choice(enemies)
            print_with_sleep("You approach the door of the house.")
            print_with_sleep(f"As you knock, the door opens, and out steps a {enemy}")
            print_with_sleep("Eep! This is not what you expected!")
            print_with_sleep(f"The {enemy} attacks you")
            print_with_sleep("You feel a bit under-prepared for this, what with only having a tiny dagger")
            fight_or_run = input("Would you like to (1) fight or (2) run away? ")
            if fight_or_run == "1":
                print_with_sleep("You try your best.....")
                print_with_sleep(f"You bravely fight the {enemy} but unfortunately meet your end")
                print_with_sleep("you are defeated...")
                break
            else:
                print_with_sleep("You manage to escape. You return to the field")
                
        elif response == "2":
            print_with_sleep("You peer cautiously into the cave")
            print_with_sleep("It turns out to be only a very small cave")
            print_with_sleep("Your eye catches a glint of metal behind a rock")
            print_with_sleep("You have found the magical Sword of Ogoroth!")
            print_with_sleep("You discard your silly old dagger and take the sword with you")
            print_with_sleep("You walk back to the field")

        else: print_with_sleep("Please enter 1 or 2")

        while True:         
                   response = input("Enter 1 to knock on the door of the house, Enter 2 to peer into the cave: ")
              
        else:
                   print_with_sleep("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    while True:
                response = input("Enter 1 to knock on the door of the house, Enter 2 to peer into the cave: ")
                if response == "1":
                    break
                elif response == "2":
                    continue



            
                
    else:
            print_with_sleep("Please enter 1 or 2")

def main():
    while True:
        print_with_sleep("You find yourself standing in an open field, filled with grass and yellow wildflowers")
        print_with_sleep("Rumor has it that a troll is somewhere around here and has been terrorizing the nearby village")
        print_with_sleep("In front of you is a house")
        print_with_sleep("To your right is a dark cave")
        print_with_sleep("In your hand, you hold your trusty (but not very effective) dagger")

        encounter_enemy()
        
        play_again = input("Would you like to play another game? (y/n): ").lower()
        if play_again == 'n':
            print_with_sleep("OK, Goodbye!")
            break
        elif play_again == 'y':
            print_with_sleep("Very good, let's restart the game!")
        else:
            print_with_sleep("Please enter 'y' or 'n'")

if __name__ == "__main__":
    main()
