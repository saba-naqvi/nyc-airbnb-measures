"""
Assignment #8 by
    Saba Naqvi
    05/31/2021
This program displays cross table statistics for a dataset of AirBNB
listings in New York City.
"""


from enum import Enum


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


class DataSet:
    """ The DataSet class will present summary tables based on
    information imported from a .csv file.
    """
    class Categories(Enum):
        LOCATION = 0
        PROPERTY_TYPE = 1

    class Stats(Enum):
        MIN = 1
        AVG = 2
        MAX = 3

    class EmptyDatasetError(Exception):
        pass

    class NoMatchingItemsError(Exception):
        pass

    copyright = "No copyright has been set."

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""
        self._labels = {
            DataSet.Categories.LOCATION: set(),
            DataSet.Categories.PROPERTY_TYPE: set()
        }

    def _initialize_sets(self):
        """ Reconfigure self._data list into individual sets stored in
        self._labels dictionary.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        self._labels[DataSet.Categories.LOCATION] = set(item[0] for item in
                                                        self._data)
        self._labels[DataSet.Categories.PROPERTY_TYPE] = set(item[1] for item in
                                                             self._data)

    def display_cross_table(self, stat: Stats):
        """ Print tables displaying either minimum, average, or maximum
        rent values for listing data extracted from self._data.

        Keyword argument:
            stat: an enum of class Stats that enumerates the statistics
            calculated in _cross_table_statistics
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        location_list = list(self._labels[DataSet.Categories.LOCATION])
        property_list = list(self._labels[DataSet.Categories.PROPERTY_TYPE])
        print("_______________", end="")
        for property_type in property_list:
            print(f"{property_type:_<20}", end="")
        print()
        for loc in location_list:
            print(f"{loc:<15}", end="")
            for property_type in property_list:
                try:
                    values = self._cross_table_statistics(loc, property_type)
                except DataSet.NoMatchingItemsError:
                    not_applicable = "N/A"
                    print(f"$ {not_applicable:<18}", end="")
                    continue
                if stat == DataSet.Stats.MIN:
                    print(f"$ {values[0]:<18.2f}", end="")
                elif stat == DataSet.Stats.AVG:
                    print(f"$ {values[1]:<18.2f}", end="")
                elif stat == DataSet.Stats.MAX:
                    print(f"$ {values[2]:<18.2f}", end="")
            print()

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        if type(header) is str:
            if not header.isnumeric() and len(header) <= 30:
                self._header = header
            else:
                raise ValueError

    def load_default_data(self):
        """ Load sample data into self._data. """
        self._data = [("Staten Island", "Private room", 70),
                      ("Brooklyn", "Private room", 50),
                      ("Bronx", "Private room", 40),
                      ("Brooklyn", "Entire home/apt", 150),
                      ("Manhattan", "Private room", 125),
                      ("Manhattan", "Entire home/apt", 196),
                      ("Brooklyn", "Private room", 110),
                      ("Manhattan", "Entire home/apt", 170),
                      ("Manhattan", "Entire home/apt", 165),
                      ("Manhattan", "Entire home/apt", 150),
                      ("Manhattan", "Entire home/apt", 100),
                      ("Brooklyn", "Private room", 65),
                      ("Queens", "Entire home/apt", 350),
                      ("Manhattan", "Private room", 98),
                      ("Brooklyn", "Entire home/apt", 200),
                      ("Brooklyn", "Entire home/apt", 150),
                      ("Brooklyn", "Private room", 99),
                      ("Brooklyn", "Private room", 120)]
        self._initialize_sets()

    def _cross_table_statistics(self, descriptor_one: str, descriptor_two: str):
        """ Given a label from each category, calculate summary
        statistics for the items matching both labels. Returns a tuple
        of minimum, average, and maximum from the matching rows.

        Keyword arguments:
            descriptor_one: a string representing the first category
            descriptor_two: a string representing the second category
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        value_list = [item[2] for item in self._data if
                      item[0] == descriptor_one and item[1] == descriptor_two]
        if len(value_list) == 0:
            raise DataSet.NoMatchingItemsError
        return min(value_list), (sum(value_list) / len(value_list)), \
            max(value_list)


def print_menu():
    """ Display the main menu text. """
    print("Main Menu")
    print("1 - Print Minimum Rent by Location and Property Type")
    print("2 - Print Average Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu(dataset: DataSet):
    """ Present user with options to access the AirBNB dataset.

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
            try:
                dataset.display_cross_table(DataSet.Stats.MIN)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
        elif int_selection == 2:
            try:
                dataset.display_cross_table(DataSet.Stats.AVG)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
        elif int_selection == 3:
            try:
                dataset.display_cross_table(DataSet.Stats.MAX)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
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
            dataset.load_default_data()
        elif int_selection == 9:
            print("Thanks for using the database. See you soon!")
            break
        else:
            print("Please enter a value between 1 and 9.")


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


if __name__ == "__main__":
    main()


"""
Please enter your name: Saba
Hello, Saba! It's nice to meet you.
What is your home currency? EUR
Enter a header for the menu: Saba's AirBNB Database
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
Saba's AirBNB Database
Main Menu
1 - Print Minimum Rent by Location and Property Type
2 - Print Average Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 1
Please load data first.
Saba's AirBNB Database
Main Menu
1 - Print Minimum Rent by Location and Property Type
2 - Print Average Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 8
Saba's AirBNB Database
Main Menu
1 - Print Minimum Rent by Location and Property Type
2 - Print Average Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 1
_______________Entire home/apt_____Private room________
Bronx          $ N/A               $ 40.00             
Staten Island  $ N/A               $ 70.00             
Brooklyn       $ 150.00            $ 50.00             
Queens         $ 350.00            $ N/A               
Manhattan      $ 100.00            $ 98.00             
Saba's AirBNB Database
Main Menu
1 - Print Minimum Rent by Location and Property Type
2 - Print Average Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 2
_______________Entire home/apt_____Private room________
Bronx          $ N/A               $ 40.00             
Staten Island  $ N/A               $ 70.00             
Brooklyn       $ 166.67            $ 88.80             
Queens         $ 350.00            $ N/A               
Manhattan      $ 156.20            $ 111.50            
Saba's AirBNB Database
Main Menu
1 - Print Minimum Rent by Location and Property Type
2 - Print Average Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 3
_______________Entire home/apt_____Private room________
Bronx          $ N/A               $ 40.00             
Staten Island  $ N/A               $ 70.00             
Brooklyn       $ 200.00            $ 120.00            
Queens         $ 350.00            $ N/A               
Manhattan      $ 196.00            $ 125.00            
Saba's AirBNB Database
Main Menu
1 - Print Minimum Rent by Location and Property Type
2 - Print Average Rent by Location and Property Type
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
