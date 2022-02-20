"""
Assignment #6 by
    Saba Naqvi
    05/17/2021
This program greets the user, launches a currency table and menu, and
uses a class object to generate a user-defined header.
"""


class DataSet:
    """ Define methods for user construction of AirBNB menu header. """

    copyright = "No copyright has been set."

    def __init__(self, header=""):
        """ Construct the _header instance attribute according to
        setter method defined in the class.

        Keyword argument:
            header: a string representing the header entered by the user,
            which defaults to an empty string
        """
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""

    @property
    def header(self):
        """ Get the _header instance attribute. """
        return self._header

    @header.setter
    def header(self, header: str):
        """ Set the _header instance attribute and raise exceptions
        based on user input.

        Keyword argument:
            header: a string representing the header set by the user
        """
        if type(header) is str:
            if not header.isnumeric() and len(header) <= 30:
                self._header = header
            else:
                raise ValueError


conversions = {
        "USD": 1.0,
        "EUR": 0.9,
        "CAD": 1.4,
        "GBP": 0.8,
        "CHF": 0.95,
        "NZD": 1.66,
        "AUD": 1.62,
        "JPY": 107.92
    }


home_currency = ""


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """ Convert from one unit of currency to another.

    Keyword arguments:
        quantity: a float representing the amount of currency to
        be converted
        source_curr: a three-letter currency identifier string
        from the conversions dictionary (currency before exchange)
        target_curr: a three-letter currency identifier string
        from the conversions dictionary (currency after exchange)
    """
    return (quantity / conversions[source_curr]) * conversions[target_curr]


def currency_options(base_curr: str):
    """ Use the currency_converter() function to convert a range of
    currency values to all other currency units in the conversions
    dictionary.

    Keyword argument:
        base_curr: a three-letter currency identifier string
        from the conversions dictionary (currency before exchange)
    """
    print(f"Options for converting from {base_curr}:")
    print(f"{base_curr:<10}", end="")
    for curr_labels in conversions:
        if curr_labels == base_curr:
            continue
        print(f"{curr_labels:<10}", end="")
    print()
    for starting_quantities in range(10, 100, 10):
        print(f"{starting_quantities:<10.2f}", end="")
        for output_curr in conversions:
            converted_result = currency_converter(starting_quantities,
                                                  base_curr, output_curr)
            if base_curr == output_curr:
                continue
            print(f"{converted_result:<10.2f}", end="")
        print()


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


def menu(dataset: DataSet):
    """ Display conversion table with header and obtain user's menu
    options.

    Keyword argument:
        dataset: a parameter of class DataSet that accesses DataSet
        attributes
    """
    currency_options(home_currency)
    print(f"{dataset.copyright}")
    while True:
        print(f"{dataset.header}")
        print_menu()
        try:
            int_selection = int(input("What is your choice? "))
        except ValueError:
            print("Next time please enter a number.")
            continue
        if int_selection == 1:
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
        elif int_selection == 9:
            print("Thanks for using the database. See you soon!")
            break
        else:
            print("Please enter a value between 1 and 9.")


def main():
    """ Greet user and launch the menu. """
    DataSet.copyright = "Copyright Saba Naqvi"
    air_bnb = DataSet()
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}!", "It's nice to meet you.")
    while True:
        global home_currency
        home_currency = input("What is your home currency? ")
        if home_currency in conversions:
            break
        else:
            continue
    while True:
        try:
            air_bnb.header = input("Enter a header for the menu: ")
            break
        except ValueError:
            continue
    menu(air_bnb)


def unit_test():
    """ Test DataSet class attribute and methods. """
    # test constructor with default parameter --> empty string
    test1 = DataSet()
    if test1.header == "":
        print(f"Testing constructor with default parameter: Pass")
    else:
        print(f"Testing constructor with default parameter: Fail")
    # test constructor with valid header argument --> valid header
    test2 = DataSet("Cool Correct Header")
    if test2.header == "Cool Correct Header":
        print(f"Testing constructor with valid header argument: Pass")
    else:
        print(f"Testing constructor with valid header argument: Fail")
    # test constructor with invalid header argument --> empty string
    test3 = DataSet("This Header Is Much Longer Than 30 Characters")
    if test3.header == "":
        print(f"Testing constructor with invalid header argument: Pass")
    else:
        print(f"Testing constructor with invalid header argument: Fail")
    # test setter with valid assignment --> header changed
    test2.header = "A Valid Header Assignment"
    if test2.header == "A Valid Header Assignment":
        print(f"Testing setter with valid assignment: Pass")
    elif test2.header == "Cool Correct Header":
        print(f"Testing setter with valid assignment: Fail")
    else:
        print(f"Testing setter with valid assignment: Fail")
    # test setter with invalid assignment --> header unchanged
    test2.header = 12345
    if test2.header == 12345:
        print(f"Testing setter with invalid assignment: Fail")
    elif test2.header == "A Valid Header Assignment":
        print(f"Testing setter with invalid assignment: Pass")
    else:
        print(f"Testing setter with invalid assignment: Fail")
    # test copyright class attribute
    print(f"Setting DataSet.copyright = 'Copyright Saba Naqvi'")
    DataSet.copyright = "Copyright Saba Naqvi"
    if DataSet.copyright == "Copyright Saba Naqvi":
        print(f"Checking that I can access this using DataSet.copyright: Pass")
    else:
        print(f"Checking that I can access this using DataSet.copyright: Fail")
    if test2.copyright == "Copyright Saba Naqvi":
        print(f"Checking that I can access this using a test object: Pass")
    else:
        print(f"Checking that I can access this using a test object: Fail")
    print()


if __name__ == "__main__":
    unit_test()
    main()


"""
Testing constructor with default parameter: Pass
Testing constructor with valid header argument: Pass
Testing constructor with invalid header argument: Pass
Testing setter with valid assignment: Pass
Testing setter with invalid assignment: Pass
Setting DataSet.copyright = 'Copyright Saba Naqvi'
Checking that I can access this using DataSet.copyright: Pass
Checking that I can access this using a test object: Pass

Please enter your name: Saba
Hello, Saba! It's nice to meet you.
What is your home currency? EUR
Enter a header for the menu: Welcome to the (AirBNB) Machine
Options for converting from EUR:
EUR       USD       CAD       GBP       CHF       NZD       AUD       JPY       
10.00     11.11     15.56     8.89      10.56     18.44     18.00     1199.11   
20.00     22.22     31.11     17.78     21.11     36.89     36.00     2398.22   
30.00     33.33     46.67     26.67     31.67     55.33     54.00     3597.33   
40.00     44.44     62.22     35.56     42.22     73.78     72.00     4796.44   
50.00     55.56     77.78     44.44     52.78     92.22     90.00     5995.56   
60.00     66.67     93.33     53.33     63.33     110.67    108.00    7194.67   
70.00     77.78     108.89    62.22     73.89     129.11    126.00    8393.78   
80.00     88.89     124.44    71.11     84.44     147.56    144.00    9592.89   
90.00     100.00    140.00    80.00     95.00     166.00    162.00    10792.00  
Copyright Saba Naqvi
Welcome to the AirBNB Machine
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
Thanks for using the database. See you soon!
"""
