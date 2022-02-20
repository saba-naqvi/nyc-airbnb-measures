"""
Final Assignment by
    Saba Naqvi
    06/23/2021
This program uses a dataset of 2019 New York City AirBNB listings to
calculate and display various rental statistics.
"""


import csv
from copy import deepcopy
from enum import Enum


filename = './AB_NYC_2019.csv'


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

    class EmptyDatasetError(Exception):
        pass

    class NoMatchingItemsError(Exception):
        pass

    copyright = "No copyright has been set."

    class Categories(Enum):
        LOCATION = 0
        PROPERTY_TYPE = 1

    class Stats(Enum):
        MIN = 0
        AVG = 1
        MAX = 2

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""
        self._labels = {DataSet.Categories.LOCATION: set(),
                        DataSet.Categories.PROPERTY_TYPE: set()}
        self._active_labels = {DataSet.Categories.LOCATION: set(),
                               DataSet.Categories.PROPERTY_TYPE: set()}

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

    @staticmethod
    def _alternate_category_type(category: Categories):
        """ Return alternate object in Categories enum. """
        if category == DataSet.Categories.LOCATION:
            return DataSet.Categories.PROPERTY_TYPE
        if category == DataSet.Categories.PROPERTY_TYPE:
            return DataSet.Categories.LOCATION

    def _initialize_sets(self):
        """ Reconfigure self._data list into individual sets stored in
        self._labels and self._active_labels dictionaries.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        for category in self.Categories:
            self._labels[category] = set([item[category.value] for item
                                          in self._data])
            self._active_labels[category] = self._labels[category].copy()

    def load_file(self):
        """ Load 2019 NYC AirBNB data into self._data. """
        global filename
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            my_list = [row[1:4] for row in csv_reader]
        my_list.remove(my_list[0])
        my_new_list = [[row[0], row[1], int(row[2])] for row in my_list]
        self._data = deepcopy(my_new_list)
        self._initialize_sets()
        print(f"{len(self._data)} lines loaded")
        return len(self._data)

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

    def _table_statistics(self, row_category: Categories, label: str):
        """ Given a category label as well as opposing label from
        self._active_labels, calculate summary statistics based on
        matching tuples in self._data; returns a tuple of minimum,
        average, and maximum.

        Keyword arguments:
            row_category: a Categories enum representing the category
            from which 'label' hails
            label: a string representing an object from the chosen
            'row_category'
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        filter_one = [item for item in self._data
                      if item[row_category.value] == label]
        alternate_category = self._alternate_category_type(row_category)
        filter_two = [item[2] for item in filter_one
                      if item[alternate_category.value]
                      in self._active_labels[alternate_category]]
        if len(filter_two) == 0:
            raise DataSet.NoMatchingItemsError
        return min(filter_two), (sum(filter_two) / len(filter_two)), \
            max(filter_two)

    def display_field_table(self, rows: Categories):
        """ Given a category from Dataset.Categories, produce a table
        that displays summary statistics for each active label in that
        category.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        rows_list = list(self._labels[rows])
        columns_list = ["Minimum", "Average", "Maximum"]
        print("The following data are from properties matching these "
              "criteria:")
        for items in self._active_labels[DataSet._alternate_category_type(rows)]:
            print(f"- {items}")
        print("                  ", end="")
        for column in columns_list:
            print(f"{column:<15}", end="")
        print()
        for label in rows_list:
            print(f"{label:<18}", end="")
            for index in range(3):
                try:
                    statistics = self._table_statistics(rows, label)
                    print(f"$ {statistics[index]:<13.2f}", end="")
                except DataSet.NoMatchingItemsError:
                    print(f"  {'N/A':<13}", end="")
            print()

    def _cross_table_statistics(self, descriptor_one: str, descriptor_two: str):
        """ Given a label from each category, calculate summary
        statistics for the items matching both labels; returns a tuple
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

    def display_cross_table(self, stat: Stats):
        """ Given a stat from Dataset.Stats, produce a table that shows
        the value of that stat for every pair of labels from the two
        categories.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        location_list = list(self._labels[DataSet.Categories.LOCATION])
        property_list = list(self._labels[DataSet.Categories.PROPERTY_TYPE])
        print("               ", end="")
        for property_type in property_list:
            print(f"{property_type:<20}", end="")
        print()
        for loc in location_list:
            print(f"{loc:<15}", end="")
            for property_type in property_list:
                try:
                    values = self._cross_table_statistics(loc, property_type)[stat.value]
                    print(f"$ {values:<18.2f}", end="")
                except DataSet.NoMatchingItemsError:
                    print(f"  {'N/A':<18}", end="")
            print()

    def get_labels(self, category: Categories):
        """ Return a list of labels for a given category. """
        if not self._data:
            raise DataSet.EmptyDatasetError
        return list(self._labels[category])

    def get_active_labels(self, category: Categories):
        """ Return a list of active labels for a given category. """
        if not self._data:
            raise DataSet.EmptyDatasetError
        return list(self._active_labels[category])

    def toggle_active_label(self, category: Categories, descriptor: str):
        """ Given a category and label, toggle the label between active
        and inactive.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError
        if descriptor not in self._labels[category]:
            raise KeyError
        if descriptor in self._active_labels[category]:
            self._active_labels[category].discard(descriptor)
        else:
            self._active_labels[category].add(descriptor)


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
    """ Present user with options to access the AirBNB dataset. """
    currency_options(home_currency)
    print()
    print(f"{dataset.copyright}")
    while True:
        print()
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
            try:
                dataset.display_field_table(DataSet.Categories.LOCATION)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
        elif int_selection == 5:
            try:
                dataset.display_field_table(DataSet.Categories.PROPERTY_TYPE)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
        elif int_selection == 6:
            try:
                manage_filters(dataset, dataset.Categories.LOCATION)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
        elif int_selection == 7:
            try:
                manage_filters(dataset, dataset.Categories.PROPERTY_TYPE)
            except dataset.EmptyDatasetError:
                print("Please load data first.")
                continue
        elif int_selection == 8:
            dataset.load_file()
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


def manage_filters(dataset: DataSet, category: DataSet.Categories):
    """ Allow the user to see all the labels in a category, and
    whether they are active. The user can toggle the active status of
    any label.
    Note: dataset.get_active_labels() may raise EmptyDatasetError
    """
    static_labels = {number: label for number, label in
                     enumerate(dataset.get_labels(category), 1)}
    while True:
        active_labels = dataset.get_active_labels(category)
        print("The following labels are in the dataset:")
        for number, label in static_labels.items():
            print(f"{number}: {label:18}"
                  f"{'ACTIVE' if label in active_labels else 'INACTIVE'}")
        selection = input("Please select an item to toggle or enter a blank "
                          "line when you are finished: ")
        if selection == '':
            break
        try:
            int_selection = int(selection)
        except ValueError:
            print("Please enter a number or a blank line.")
            continue
        if int_selection in static_labels:
            dataset.toggle_active_label(category, static_labels[int_selection])
        else:
            print("Please enter a number that corresponds to a menu item.")


def main():
    """ Greet user and launch the menu. """
    DataSet.copyright = "Copyright 2021 Saba Naqvi"
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
What is your home currency? AUD
Enter a header for the menu: Final AirBNB Database
Options for converting from AUD:
AUD       USD       EUR       CAD       GBP       CHF       NZD       JPY       
10.00     6.17      5.56      8.64      4.94      5.86      10.25     666.17    
20.00     12.35     11.11     17.28     9.88      11.73     20.49     1332.35   
30.00     18.52     16.67     25.93     14.81     17.59     30.74     1998.52   
40.00     24.69     22.22     34.57     19.75     23.46     40.99     2664.69   
50.00     30.86     27.78     43.21     24.69     29.32     51.23     3330.86   
60.00     37.04     33.33     51.85     29.63     35.19     61.48     3997.04   
70.00     43.21     38.89     60.49     34.57     41.05     71.73     4663.21   
80.00     49.38     44.44     69.14     39.51     46.91     81.98     5329.38   
90.00     55.56     50.00     77.78     44.44     52.78     92.22     5995.56   

Copyright 2021 Saba Naqvi

Final AirBNB Database
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

Final AirBNB Database
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
48895 lines loaded

Final AirBNB Database
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
               Entire home/apt     Shared room         Private room        
Brooklyn       $ 0.00              $ 0.00              $ 0.00              
Manhattan      $ 0.00              $ 10.00             $ 10.00             
Staten Island  $ 48.00             $ 13.00             $ 20.00             
Bronx          $ 28.00             $ 20.00             $ 0.00              
Queens         $ 10.00             $ 11.00             $ 10.00             

Final AirBNB Database
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
               Entire home/apt     Shared room         Private room        
Brooklyn       $ 178.33            $ 50.53             $ 76.50             
Manhattan      $ 249.24            $ 88.98             $ 116.78            
Staten Island  $ 173.85            $ 57.44             $ 62.29             
Bronx          $ 127.51            $ 59.80             $ 66.79             
Queens         $ 147.05            $ 69.02             $ 71.76             

Final AirBNB Database
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
               Entire home/apt     Shared room         Private room        
Brooklyn       $ 10000.00          $ 725.00            $ 7500.00           
Manhattan      $ 10000.00          $ 1000.00           $ 9999.00           
Staten Island  $ 5000.00           $ 150.00            $ 300.00            
Bronx          $ 1000.00           $ 800.00            $ 2500.00           
Queens         $ 2600.00           $ 1800.00           $ 10000.00          

Final AirBNB Database
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
What is your choice? 4
The following data are from properties matching these criteria:
- Entire home/apt
- Shared room
- Private room
                  Minimum        Average        Maximum        
Brooklyn          $ 0.00         $ 124.38       $ 10000.00     
Manhattan         $ 0.00         $ 196.88       $ 10000.00     
Staten Island     $ 13.00        $ 114.81       $ 5000.00      
Bronx             $ 0.00         $ 87.50        $ 2500.00      
Queens            $ 10.00        $ 99.52        $ 10000.00     

Final AirBNB Database
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
What is your choice? 5
The following data are from properties matching these criteria:
- Brooklyn
- Bronx
- Manhattan
- Staten Island
- Queens
                  Minimum        Average        Maximum        
Entire home/apt   $ 0.00         $ 211.79       $ 10000.00     
Shared room       $ 0.00         $ 70.13        $ 1800.00      
Private room      $ 0.00         $ 89.78        $ 10000.00     

Final AirBNB Database
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
What is your choice? 6
The following labels are in the dataset:
1: Brooklyn          ACTIVE
2: Manhattan         ACTIVE
3: Staten Island     ACTIVE
4: Bronx             ACTIVE
5: Queens            ACTIVE
Please select an item to toggle or enter a blank line when you are finished: 3
The following labels are in the dataset:
1: Brooklyn          ACTIVE
2: Manhattan         ACTIVE
3: Staten Island     INACTIVE
4: Bronx             ACTIVE
5: Queens            ACTIVE
Please select an item to toggle or enter a blank line when you are finished: 5
The following labels are in the dataset:
1: Brooklyn          ACTIVE
2: Manhattan         ACTIVE
3: Staten Island     INACTIVE
4: Bronx             ACTIVE
5: Queens            INACTIVE
Please select an item to toggle or enter a blank line when you are finished: 

Final AirBNB Database
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
What is your choice? 5
The following data are from properties matching these criteria:
- Brooklyn
- Bronx
- Manhattan
                  Minimum        Average        Maximum        
Entire home/apt   $ 0.00         $ 217.95       $ 10000.00     
Shared room       $ 0.00         $ 70.48        $ 1000.00      
Private room      $ 0.00         $ 93.29        $ 9999.00      

Final AirBNB Database
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
