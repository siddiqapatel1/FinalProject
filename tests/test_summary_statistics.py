import pandas as pd
import os
import unittest

class TestSummaryStatistics(unittest.TestCase):
    """
    Unit tests for summary statistics calculations and related file outputs.
    """

    def setUp(self):
        """
        Set up mock data and paths for testing.
        """
        self.data_path = './data/Food_Prices_For_Nutrition.xlsx'
        self.mock_data = {
            'Cost of an energy sufficient diet': [0.5, 1.0, 1.5],
            'Cost of a nutrient adequate diet': [2.0, 2.5, 3.0],
            'Cost of a healthy diet': [3.5, 4.0, 4.5]
        }

    def test_required_columns_exist(self):
        """
        Test if the required columns for summary statistics exist in the dataset.
        """
        # Load the main data sheet
        main_data = pd.read_excel(self.data_path, sheet_name='Data')

        # Define the required columns
        required_columns = [
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet',
            'Percent of the population who cannot afford sufficient calories',
            'Percent of the population who cannot afford nutrient adequacy',
            'Percent of the population who cannot afford a healthy diet'
        ]

        # Assert each column exists in the dataset
        for column in required_columns:
            self.assertIn(column, main_data.columns, f"Missing column: {column}")

    def test_summary_statistics_calculations(self):
        """
        Test if the summary statistics for diet costs are calculated correctly.
        """
        # Create a DataFrame from mock data
        df = pd.DataFrame(self.mock_data)

        # Calculate summary statistics
        stats = df.describe()

        # Assert that the calculated mean values match the expected results
        self.assertEqual(stats.loc['mean', 'Cost of an energy sufficient diet'], 1.0)
        self.assertEqual(stats.loc['mean', 'Cost of a nutrient adequate diet'], 2.5)
        self.assertEqual(stats.loc['mean', 'Cost of a healthy diet'], 4.0)

    def test_cost_ratios(self):
        """
        Test if cost ratios (Healthy vs Energy Sufficient, Healthy vs Nutrient Adequate)
        are calculated correctly.
        """
        # Create a DataFrame from mock data
        df = pd.DataFrame(self.mock_data)

        # Calculate cost ratios
        df['Healthy vs Energy Sufficient'] = df['Cost of a healthy diet'] / df['Cost of an energy sufficient diet']
        df['Healthy vs Nutrient Adequate'] = df['Cost of a healthy diet'] / df['Cost of a nutrient adequate diet']

        # Assert that the calculated ratios match the expected values
        self.assertAlmostEqual(df['Healthy vs Energy Sufficient'].iloc[0], 7.0)
        self.assertAlmostEqual(df['Healthy vs Nutrient Adequate'].iloc[1], 1.6)

    def test_output_files(self):
        """
        Test if summary statistics CSV files are saved in the correct folder.
        """
        # Define the expected file paths
        expected_files = [
            './summary_stats_results/diet_cost_summary.csv',
            './summary_stats_results/affordability_summary.csv',
            './summary_stats_results/cost_ratios_summary.csv'
        ]

        # Assert that each file exists in the expected folder
        for file_path in expected_files:
            self.assertTrue(os.path.exists(file_path), f"Output file not found: {file_path}")

if __name__ == '__main__':
    unittest.main()
