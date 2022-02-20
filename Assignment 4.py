"""
Assignment #4 by
    Saba Naqvi
    05/03/2021
This program converts between currencies based on exchange rate
values in a global dictionary, and does unit testing to test for various
edge cases.
"""


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


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """ This function converts values from one currency to another.

    Args:
        quantity (float): amount of money in original currency
        source_curr (str): original currency
        target_curr (str): currency after exchange
    """
    return (quantity / conversions[source_curr]) * conversions[target_curr]


def unit_test():
    """ This function tests various edge cases for the
    currency_converter() function.
    """
    # source_curr is not in dictionary --> KeyError
    try:
        currency_converter(100, "PKR", "USD")
        print("FAIL: Invalid source currency did not raise KeyError")
    except KeyError:
        print("PASS: Invalid source currency raises KeyError")
    # target_curr is not in dictionary --> KeyError
    try:
        currency_converter(100, "GBP", "DKK")
        print("FAIL: Invalid target currency did not raise KeyError")
    except KeyError:
        print("PASS: Invalid target currency raises KeyError")
    # convert 100 USD to EUR --> 90
    if currency_converter(100, "USD", "EUR") == 90:
        print("PASS: Conversion from USD to EUR")
    else:
        print("FAIL: currency_converter(100, 'USD', 'EUR')")
    # convert 140 CAD to USD --> 100
    if currency_converter(140, "CAD", "USD") == 100:
        print("PASS: Conversion from CAD to USD")
    else:
        print("FAIL: currency_converter(140, 'CAD', 'USD')")
    # convert 2.8 CAD to GBP --> 1.6
    if currency_converter(2.8, "CAD", "GBP") == 1.6:
        print("PASS: Conversion from CAD to GBP")
    else:
        print("FAIL: currency_converter(2.8, 'CAD', 'GBP')")


if __name__ == "__main__":
    unit_test()


"""
PASS: Invalid source currency raises KeyError
PASS: Invalid target currency raises KeyError
PASS: Conversion from USD to EUR
PASS: Conversion from CAD to USD
PASS: Conversion from CAD to GBP
"""