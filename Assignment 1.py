"""
Assignment #1 by
    Saba Naqvi
    04/12/2021
This program asks the user for their name, and then responds with a
friendly greeting using that name.
"""


def main():
    """ Obtain the user's name. """
    user_name = input("Please enter your name: ")
    print("Hello,", user_name + "!", "It's nice to meet you.")


if __name__ == "__main__":
    main()


"""
Please enter your name: Saba
Hello, Saba! It's nice to meet you.
"""
