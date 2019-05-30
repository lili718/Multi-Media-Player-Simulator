#Lia Johnson CS 172 Spring 2019
#id :Lej42
#this is the main script to HW2(Media Library simulator)
#purpose: use the classes defined in Media.py to create a media library simulator
from Media import *
if __name__ == "__main__":
    library = [Movie("Black Panther", 4.1, "Ryan Coogler","135 minutes"),
               Movie("Avengers: Endgame", 4.6, "Anthony Russo and Joe Russo", "182 minutes"),
               Movie("Captain Marvel", 2.8, "Anna Boden and Ryan Fleck", "128 minutes"),
               Movie("Little", 2.0, "Tina Gordon Chism", "109 minutes"),
               Song("7 rings", 3.6, "Ariana Grande", "Thank U, Next"),
               Song("Un-Break My Heart", 5.0, "Toni Braxton", "Secrets"),
               Song("Alright", 4.8, "Kendrick Lamar", "To Pimp a Butterfly"),
               Song("Formation", 4.0, "Beyonce", "Lemonade"),
               Picture("Man jumping the puddle", 3.2, "550 dpi"),
               Picture("The Steerage", 1.5, "280 dpi"),
               Picture("Starving Child and Vulture", 4.7, "800 dpi"),
               Picture("The Terror of War", 3.0, "470 dpi")
              ]

    def menu():
        print("\n1. Display all items in Media Library")
        print("2. Display songs only")
        print("3. Display movies only")
        print("4. Display pictures only")
        print("5. Play a song")
        print("6. Play a movie")
        print("7. Display a picture")
        print("8. Quit")
        
    print("Welcome to Lia's Media Library")
    print("-"*30)
    menu()

    userOptions = ["1", "2", "3", "4", "5", "6", "7", "8"]
    selection = input("Please enter the number associated with the action you want to perform\n")

    while selection != "8":
        if selection == "1":
            print("The Media Library currently contains:\n")
            for i in library:
                print(i)
        
        if selection == "2":
            print("The songs in the Media Library are:\n")
            for i in library:
                if i.getType() == "Song":
                    print(i)
            print()
            
        if selection == "3":
            print("The movies in the Media Library are:\n")
            for i in library:
                if i.getType() == "Movie":
                    print(i)
            print()
        
        if selection == "4":
            print("The pictures in the Media Library are:\n")
            for i in library:
                if i.getType() == "Picture":
                    print(i)
            print()
        
        if selection == "5":
            sName = input("Please enter the name of the song you wish to play\n")
            available = False
            for i in library:
                if i.getType() == "Song" and i.getName() == sName:
                    i.play()
                    available = True
            if available == False:
                print("\nWe are sorry, but the song you have asked for is not in the media library")
            print()
            
        if selection == "6":
            mName = input("Please enter the name of the movie you wish to play\n")
            available = False
            for i in library:
                if i.getType() == "Movie" and i.getName() == mName:
                    i.play()
                    available = True
            if available == False:
                print("\nWe are sorry, but the movie you have asked for is not in the media library")
            print()

        if selection == "7":
            pName = input("Please enter the name of the picture you wish to play\n")
            available = False
            for i in library:
                if i.getType() == "Picture" and i.getName() == pName:
                    i.show()
                    available = True
            if available == False:
                print("\nWe are sorry, but the picture you have asked for is not in the media library")
            print()
        
        if selection not in userOptions:
            print("not a valid input. Please try again\n")
            
        menu()
        selection = input("Please enter the number associated with the action you want to perform\n")

    else:
        print("Quiting Media Library")
            
        
