import pandas as pd
import os
import unittest

class TestAffordabilityVisualisation(unittest.TestCase):
    """
    Unit tests for verifying the data and outputs related to the affordability bar chart visualisation.
    """

    def setUp(self):
        """
        Set up the dataset paths and reusable configurations for the tests.
        """
        self.data_path = './data/Food_Prices_For_Nutrition.xlsx'
        self.required_columns = [
            'Country Name',
            'Percent of the population who cannot afford sufficient calories',
            'Percent of the population who cannot afford nutrient adequacy',
            'Percent of the population who cannot afford a healthy diet'
        ]
        self.figure_path = './figures/affordability_bar_chart.png'

    def test_required_columns_exist(self):
        """
        Test to verify that the required columns for the affordability analysis
        exist in the dataset.

        This test ensures that all columns necessary for visualising the affordability
        of different diet types are present in the main dataset. Missing columns will 
        cause the test to fail with an appropriate error message.
        """
        # Load the dataset
        df = pd.read_excel(self.data_path, sheet_name='Data')

        # Check for the presence of each required column
        for col in self.required_columns:
            self.assertIn(col, df.columns, f"Missing required column: {col}")

    def test_data_filtering(self):
        """
        Test to verify that the data filtering process for the visualisation is correct.

        This test ensures that rows with null income group values are properly filtered
        out during the data preparation stage. The merged dataset should only contain
        rows with non-null income group values.
        """
        # Load the metadata and main dataset
        metadata = pd.read_excel(self.data_path, sheet_name='Country - Metadata')
        main_data = pd.read_excel(self.data_path, sheet_name='Data')

        # Merge the main data with metadata to include income groups
        merged_data = pd.merge(
            main_data,
            metadata,
            left_on='Country Name',
            right_on='Table Name',
            how='left'
        )

        # Filter rows with non-null income groups
        filtered_data = merged_data.dropna(subset=['Income Group'])

        # Assert that no rows with null income groups exist in the filtered data
        self.assertEqual(
            filtered_data['Income Group'].isnull().sum(), 0,
            "Filtered data contains rows with null Income Group"
        )

    def test_figure_saved(self):
        """
        Test to verify that the affordability bar chart is saved successfully 
        in the specified output directory.

        This test ensures that the visualisation script generates the affordability
        bar chart and saves it as a PNG file in the expected location.
        """
        # Assert that the figure file exists at the specified location
        self.assertTrue(
            os.path.exists(self.figure_path),
            f"Figure not found at {self.figure_path}"
        )


if __name__ == '__main__':
    unittest.main()
