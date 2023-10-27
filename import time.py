import time
import random

enemies = ["Devil Fairy", "Bad Pirates", "Big Dragon"]

while True:  # This outer loop allows the game to restart
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(2)
    print(f"Rumor has it that a {enemy} is somewhere around here and has been terrorizing the nearby village.")
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print("In your hand, you hold your trusty (but not very effective) dagger.")
    time.sleep(2)

    while True: # This second loop allows the game to back to make choices forcing user to make decision.
        response = input("Enter 1 to knock on the door of the house, "
                         "Enter 2 to peer into the cave: ")

        if response == "1":
            print("You approach the door of the house.")
            time.sleep(2)
            print("As you knock, the door opens, and out steps a", random.choice(enemies))
            time.sleep(2)
            print("Eep! This is not what you expected!")
            time.sleep(2)
            print("The {enemy} attacks you!")
            time.sleep(2)
            print("You feel a bit under-prepared for this, what with only having a tiny dagger.")
            time.sleep(2)

            while True:
                response= input(fight_or_run)
            

        elif response == "2":
            print("You peer cautiously into the cave.")
            time.sleep(2)
            print("It turns out to be only a very small cave.")
            time.sleep(2)
            print("Your eye catches a glint of metal behind a rock.")
            time.sleep(2)
            print("You have found the magical Sword of Ogoroth!")
            time.sleep(2)
            print("You discard your silly old dagger and take the sword with you.")
            time.sleep(2)
            print("You walk back to the field.")
            
            while True: 
                     response = input("Enter 1 to knock on the door of the house, "
                                      "Enter 2 to peer into the cave: ")
                     
                        if response == "1":
                          print("You approach the door of the house.")
                          time.sleep(2)
                          print("As you knock, the door opens, and out steps a", random.choice(enemies))
                          time.sleep(2)
                          print("Eep! This is not what you expected!")
                          time.sleep(2)
                          print("The {enemy} attacks you!")
                          time.sleep(2)
                          print("You feel a bit under-prepared for this, what with only having a tiny dagger.")
                          time.sleep(2)

                        elif response == "2":
                        print("You peer cautiously into the cave.")
                        print("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
                        print("You walk back out to the field.")
                        return(response = input("Enter 1 to knock on the door of the house, "
                                      "Enter 2 to peer into the cave: ")
                     
        
    else:
        print("Please enter 1 or 2.")   
            
            
            


fight_or_run = input("Would you like to (1) fight or (2) run away? ")
            if fight_or_run == "1":
                print("You do your best...")
                print("but your dagger is no match for the {enemy}.")
                print("You have been defeated!")
                break
            elif :
                print("You run back into the field. Luckily, you don't seem to have been followed.")
                break
                return(response = input("Enter 1 to knock on the door of the house, "
                         "Enter 2 to peer into the cave: "))
)
                
                
            else:
                play_again = input("Would you like to play another game? (y/n): ").lower()
                if play_again == 'n':
                print("OK, Goodbye!")
                break
                elif play_again == 'y':
                 print("Very good, let's restart the game!")
                 restart("You find yourself standing in an open field, filled with grass and yellow wildflowers.")

            else:
            print("Please enter 'y' or 'n'.")
