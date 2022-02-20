import unittest
import Final_Assignment as fa


class TestFinalAssignment(unittest.TestCase):

    def test_dataset_row_count(self):
        test_instance = fa.DataSet()
        self.assertEqual(48895, fa.DataSet.load_file(test_instance))

    def test_bad_currencies(self):
        with self.assertRaises(KeyError):
            fa.currency_converter(10, "PKR", "NZD")
        with self.assertRaises(KeyError):
            fa.currency_converter(10, "NZD", "PKR")

    def test_data_loading_exceptions(self):
        test_instance = fa.DataSet()
        with self.assertRaises(fa.DataSet.EmptyDatasetError):
            fa.DataSet.get_labels(test_instance, fa.DataSet.Categories.LOCATION)
        with self.assertRaises(fa.DataSet.EmptyDatasetError):
            fa.DataSet.get_active_labels(test_instance, fa.DataSet.Categories.PROPERTY_TYPE)
        with self.assertRaises(fa.DataSet.EmptyDatasetError):
            fa.DataSet.toggle_active_label(test_instance, fa.DataSet.Categories.LOCATION, "Brooklyn")

    def test_data_filtering(self):
        test_instance = fa.DataSet()
        fa.DataSet.load_file(test_instance)
        test_instance.toggle_active_label(fa.DataSet.Categories.LOCATION, "Manhattan")
        test_instance.toggle_active_label(fa.DataSet.Categories.LOCATION, "Queens")
        test_instance.toggle_active_label(fa.DataSet.Categories.LOCATION, "Staten Island")
        test_instance.toggle_active_label(fa.DataSet.Categories.LOCATION, "Brooklyn")
        self.assertEqual(['Bronx'], fa.DataSet.get_active_labels(test_instance, fa.DataSet.Categories.LOCATION))


if __name__ == '__main__':
    unittest.main()
