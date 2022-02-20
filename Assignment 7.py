"""
Assignment #7 by
    Saba Naqvi
    05/24/2021
This program uses lists and tuples to generate statistics for sample
AirBNB listings.
"""


class DataSet:
    """ Define methods for user construction of AirBNB menu header. """
    copyright = "No copyright has been set."

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""

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

    class EmptyDataSetError(Exception):
        pass

    class NoMatchingItemsError(Exception):
        pass

    def _cross_table_statistics(self, descriptor_one: str, descriptor_two: str):
        """ Generate rental statistics.

         Keyword arguments:
             descriptor_one: a string representing property location
             descriptor_two: a string representing property type
        """
        if self._data is None:
            raise self.EmptyDataSetError
        elif any(descriptor_one in sublist for sublist in self._data) is False:
            raise self.NoMatchingItemsError
        elif any(descriptor_two in sublist for sublist in self._data) is False:
            raise self.NoMatchingItemsError
        else:
            prices = [listing[2] for listing in self._data
                      if descriptor_one == listing[0] and
                      descriptor_two == listing[1]]
            average_rent = sum(prices) / len(prices)
            rent_stats = (min(prices), average_rent, max(prices))
            return rent_stats

    def load_default_data(self):
        """ Load default AirBNB listing data. """
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


def unit_test():
    print("Testing _cross_table_statistics:")
    test = DataSet("Test Header")
    try:
        test._cross_table_statistics("Brooklyn", "Private Room")
    except test.EmptyDataSetError:
        print("Method raises EmptyDataSetError: Pass")
    else:
        print("Method doesn't raise EmptyDataSetError: Fail")
    test.load_default_data()
    try:
        test._cross_table_statistics("Manhattan", "Treehouse")
    except test.NoMatchingItemsError:
        print("Invalid Property Type Raises NoMatchingItemsError: Pass")
    else:
        print("Invalid Property Type Doesn't Raise NoMatchingItemsError: Fail")
    try:
        test._cross_table_statistics("New Jersey", "Private room")
    except test.NoMatchingItemsError:
        print("Invalid Borough Raises NoMatchingItemsError: Pass")
    else:
        print("Invalid Borough Doesn't Raise NoMatchingItemsError: Fail")
    try:
        test._cross_table_statistics("Queens", "Private Room")
    except test.NoMatchingItemsError:
        print("No Matching Rows Raises NoMatchingItemsError: Pass")
    else:
        print("No Matching Rows Doesn't Raise NoMatchingItems Error: Fail")
    one_match = test._cross_table_statistics("Queens", "Entire home/apt")
    if one_match == (350, 350.0, 350):
        print("One Matching Row Returns Correct Tuple: Pass")
    else:
        print("One Matching Row Doesn't Return Correct Tuple: Fail")
    multiple_match = test._cross_table_statistics("Brooklyn", "Private room")
    if multiple_match == (50, 88.8, 120):
        print("1. Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("1. Multiple Matching Rows Doesn't Return Correct Tuple: Fail")
    other_cases = test._cross_table_statistics("Manhattan", "Private room")
    if other_cases == (98, 111.5, 125):
        print("2. Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("2. Multiple Matching Rows Doesn't Return Correct Tuple: Fail")


if __name__ == "__main__":
    unit_test()


"""
Testing _cross_table_statistics:
Method raises EmptyDataSetError: Pass
Invalid Property Type Raises NoMatchingItemsError: Pass
Invalid Borough Raises NoMatchingItemsError: Pass
No Matching Rows Raises NoMatchingItemsError: Pass
One Matching Row Returns Correct Tuple: Pass
1. Multiple Matching Rows Returns Correct Tuple: Pass
2. Multiple Matching Rows Returns Correct Tuple: Pass
"""
