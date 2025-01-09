import pandas as pd
import unittest

class TestBoxplotData(unittest.TestCase):
    """
    Unit tests for validating the data and logic used in the boxplot visualisation.
    """

    def setUp(self):
        """
        Set up the dataset paths and reusable configurations for the tests.
        """
        self.data_path = './data/Food_Prices_For_Nutrition.xlsx'
        self.required_columns = [
            'Income Group',
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet'
        ]
        self.expected_diet_types = [
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet'
        ]

    def test_critical_columns_exist(self):
        """
        Test to verify that all required columns for creating the boxplot exist
        in the merged dataset. Missing columns will result in a failed test
        with an appropriate error message.
        """
        # Load the main dataset and metadata
        main_data = pd.read_excel(self.data_path, sheet_name='Data')
        country_metadata = pd.read_excel(self.data_path, sheet_name='Country - Metadata')

        # Merge the datasets to include income groups
        merged_data = pd.merge(
            main_data,
            country_metadata,
            left_on='Country Name',
            right_on='Table Name',
            how='left'
        )

        # Check if each required column is present in the merged dataset
        for column in self.required_columns:
            self.assertIn(column, merged_data.columns, f"Column '{column}' is missing from the merged dataset")

    def test_boxplot_data_validity(self):
        """
        Test to ensure the filtered data for the boxplot is valid:
        - No missing values in 'Income Group' or 'Cost' columns.
        - Data is properly reshaped and contains valid entries for all diet types.
        """
        # Load the main dataset and metadata
        main_data = pd.read_excel(self.data_path, sheet_name='Data')
        country_metadata = pd.read_excel(self.data_path, sheet_name='Country - Metadata')

        # Merge the datasets to include income groups
        merged_data = pd.merge(
            main_data,
            country_metadata,
            left_on='Country Name',
            right_on='Table Name',
            how='left'
        )

        # Reshape the data for boxplot creation
        filtered_data = merged_data.melt(
            id_vars=['Income Group'],
            value_vars=self.required_columns[1:],  # Exclude 'Income Group'
            var_name='Diet Type',
            value_name='Cost'
        )

        # Drop rows with missing values in critical columns
        filtered_data = filtered_data.dropna(subset=['Income Group', 'Cost'])

        # Validate that no missing values exist in the filtered data
        self.assertFalse(filtered_data.isnull().values.any(), "Filtered data contains missing values")

        # Validate that all diet types are present in the reshaped data
        unique_diet_types = filtered_data['Diet Type'].unique()
        for diet in self.expected_diet_types:
            self.assertIn(diet, unique_diet_types, f"Diet type '{diet}' is missing from the filtered data")

    def test_cost_values_within_expected_range(self):
        """
        Test to verify that the cost values in the filtered data fall within a 
        reasonable range (e.g., positive values).
        """
        # Load the main dataset and metadata
        main_data = pd.read_excel(self.data_path, sheet_name='Data')
        country_metadata = pd.read_excel(self.data_path, sheet_name='Country - Metadata')

        # Merge the datasets to include income groups
        merged_data = pd.merge(
            main_data,
            country_metadata,
            left_on='Country Name',
            right_on='Table Name',
            how='left'
        )

        # Reshape the data for boxplot creation
        filtered_data = merged_data.melt(
            id_vars=['Income Group'],
            value_vars=self.required_columns[1:],  # Exclude 'Income Group'
            var_name='Diet Type',
            value_name='Cost'
        )

        # Drop rows with missing values in critical columns
        filtered_data = filtered_data.dropna(subset=['Income Group', 'Cost'])

        # Assert that all cost values are positive
        self.assertTrue((filtered_data['Cost'] > 0).all(), "Filtered data contains non-positive cost values")

if __name__ == '__main__':
    unittest.main()
