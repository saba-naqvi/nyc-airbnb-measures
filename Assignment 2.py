"""
Assignment #2 by
    Saba Naqvi
    04/19/2021
This program greets the user based on their inputted name, offers the
user 9 menu options to choose from, and then
displays a unique response based on their choice.
"""


def main():
    """ Obtain the user's name, print menu options, and respond to the
    menu choice that the user inputs. """
    user_name = input("Please enter your name: ")
    print("Hello,", user_name + "!", "It's nice to meet you.")

    def print_menu():
        """ Print menu options."""
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
        """ Obtain user's menu choice and provide a response while
        handling for exceptions. """
        print_menu()
        user_selection = input("What is your choice? ")
        try:
            int_selection = int(user_selection)
        except ValueError:
            print("Next time please enter a number.")
        else:
            if int_selection == 1:
                print("Average rent functionality is not implemented "
                      "yet.")
            elif int_selection == 2:
                print("Minimum rent functionality is not implemented "
                      "yet.")
            elif int_selection == 3:
                print("Maximum rent functionality is not implemented "
                      "yet.")
            elif int_selection == 4:
                print("Location functionality is not implemented yet.")
            elif int_selection == 5:
                print("Property type functionality is not implemented "
                      "yet.")
            elif int_selection == 6:
                print("Location filtering functionality is not "
                      "implemented yet.")
            elif int_selection == 7:
                print("Property type filtering functionality is not "
                      "implemented yet.")
            elif int_selection == 8:
                print("Data loading functionality is not implemented "
                      "yet.")
            elif int_selection == 9:
                print("You're stuck here for now. But once Saba learns "
                      "more Python, you'll be able to quit.")
            else:
                print("Please enter a digit between 1 and 9.")

    menu()


if __name__ == "__main__":
    main()


"""
---Sample Run #1---
Please enter your name: Saba
Hello, Saba! It's nice to meet you.
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 5
Property type functionality is not implemented yet.

---Sample Run #2---
Please enter your name: Saba
Hello, Saba! It's nice to meet you.
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
You're stuck here for now. But once Saba learns more Python, you'll be able to quit.

---Sample Run #3---
Please enter your name: Saba
Hello, Saba! It's nice to meet you.
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 234
Please enter a digit between 1 and 9.

---Sample Run #4---
Please enter your name: Saba
Hello, Saba! It's nice to meet you.
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? I can't decide, maybe 5?
Next time please enter a number.
"""