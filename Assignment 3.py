"""
Assignment #3 by
    Saba Naqvi
    04/26/2021
This program greets the user, offers 9 menu choices, and based on the
user's choice provides a unique response and loops to let the
user choose again.
"""


def print_menu():
    """ Display the main menu text. """
    print("Main Menu")
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu():
    """ Obtain user's menu choice and respond appropriately, then loop. """
    int_selection = True
    while int_selection:
        print_menu()
        user_selection = input("What is your choice? ")
        if user_selection == "9":
            print("See you soon!")
            break
        try:
            int_selection = int(user_selection)
        except ValueError:
            print("Next time please enter a number.")
            continue
        if int_selection > 9:
            print("Please enter a number between 1 and 9.")
        elif int_selection < 1:
            print("Please enter a number between 1 and 9.")
        elif int_selection == 1:
            print("Average rent functionality is not implemented yet.")
        elif int_selection == 2:
            print("Minimum rent functionality is not implemented yet.")
        elif int_selection == 3:
            print("Maximum rent functionality is not implemented yet.")
        elif int_selection == 4:
            print("Location functionality is not implemented yet.")
        elif int_selection == 5:
            print("Property type functionality is not implemented yet.")
        elif int_selection == 6:
            print("Location filtering functionality is not implemented yet.")
        elif int_selection == 7:
            print("Property type filtering functionality is not implemented "
                  "yet.")
        elif int_selection == 8:
            print("Data loading functionality is not implemented yet.")


def main():
    """ Greet the user and launch the menu. """
    user_name = input("Please enter your name. ")
    print("Hello,", user_name + "!", "It's nice to meet you.")
    menu()


if __name__ == "__main__":
    main()


"""
Please enter your name. Saba
Hello, Saba! It's nice to meet you.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 2
Minimum rent functionality is not implemented yet.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 7
Property type filtering functionality is not implemented yet.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 13
Please enter a number between 1 and 9.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? five
Next time please enter a number.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 9
See you soon!
"""