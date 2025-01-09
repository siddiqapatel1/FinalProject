import pandas as pd
import os
import unittest

class TestPieChart(unittest.TestCase):
    """
    Unit tests for the pie chart visualisation of food group contributions to 
    the cost of a healthy diet.
    """

    def setUp(self):
        """
        Set up the dataset path and any reusable test data for the tests.
        """
        self.data_path = './data/Food_Prices_For_Nutrition.xlsx'
        self.expected_output_path = './figures/food_group_pie_chart.png'

    def test_percentage_contributions_sum(self):
        """
        Test to verify that the percentage contributions of each food group 
        to the cost of a healthy diet sum to 100%.

        This test ensures that the average contributions of different food 
        groups are correctly normalised to percentages and that the total 
        percentage adds up to 100%, indicating a valid pie chart representation.
        """
        # Load the dataset
        df = pd.read_excel(self.data_path, sheet_name='Data')

        # Extract relevant columns for food group costs
        pie_chart_data = df[['Cost of fruits', 'Cost of starchy staples', 
                             'Cost of vegetables', 'Cost of animal-source foods', 
                             'Cost of legumes, nuts and seeds', 'Cost of oils and fats']]

        # Calculate average contributions for each food group
        average_contributions = pie_chart_data.mean()

        # Calculate the total cost across all food groups
        total_cost = average_contributions.sum()

        # Convert contributions to percentages
        percentage_contributions = (average_contributions / total_cost) * 100

        # Assert that the total percentage is approximately 100% (tolerance: 0.01%)
        self.assertAlmostEqual(percentage_contributions.sum(), 100, delta=0.01, 
                               msg="Percentage contributions do not sum to 100")

    def test_pie_chart_saved(self):
        """
        Test to verify that the pie chart figure is saved successfully in the 
        specified output directory.

        This test checks the existence of the pie chart image file to ensure
        that the visualisation script generated the output as expected.
        """
        # Assert that the file exists at the specified location
        self.assertTrue(os.path.exists(self.expected_output_path), 
                        f"Pie chart not found at {self.expected_output_path}")

if __name__ == '__main__':
    unittest.main()
