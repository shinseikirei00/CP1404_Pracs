"""
Replace the contents of this module docstring with your own details.
"""
MENU = """L - List Songs
    A - Add New Song
    C - Complete a Song
    Q - Quit"""

def main():
    in_file = open("songs.csv")
    for line in in_file:
        list.append(line)

    print("Songs To Learn 1.0 - by <Jan Crooks>")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # pass list into list_of_songs fucntion
            #
            #
        elif choice == "A":
            # pass list into add_new_song fucntion
            #
            #
        elif choice == "C":
            # pass list into complete_song fucntion
            #
            #
        elif choice == "Q":
            #print amount of songs saved into songs.csv
            print("Have a nice Day")

        else:
            print("Invalid option")
        print(MENU)



def list_of_songs():
    #list out songs from csv file
    #return list


main()

