import pandas as pd
import os

# Test 1: Verify Required Columns
def test_required_columns_exist():
    """
    Test to verify that the required columns for the affordability analysis
    exist in the dataset.

    This test ensures that all columns necessary for visualizing the affordability
    of different diet types are present in the main dataset. Missing columns will 
    cause the test to fail with an appropriate error message.
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load the dataset
    df = pd.read_excel(data_path, sheet_name='Data')

    # Define the required columns
    required_columns = [
        'Country Name',
        'Percent of the population who cannot afford sufficient calories',
        'Percent of the population who cannot afford nutrient adequacy',
        'Percent of the population who cannot afford a healthy diet'
    ]

    # Check for the presence of each required column
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

# Test 2: Verify Data Filtering for the Visualisation
def test_data_filtering():
    """
    Test to verify that the data filtering process for the visualization is correct.

    This test ensures that rows with null income group values are properly filtered
    out during the data preparation stage. The merged dataset should only contain
    rows with non-null income group values.
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load the metadata and main dataset
    metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    main_data = pd.read_excel(data_path, sheet_name='Data')

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
    assert filtered_data['Income Group'].isnull().sum() == 0, \
        "Filtered data contains rows with null Income Group"

# Test 3: Verify Figure Output
def test_figure_saved():
    """
    Test to verify that the affordability bar chart is saved successfully 
    in the specified output directory.

    This test ensures that the visualization script generates the affordability
    bar chart and saves it as a PNG file in the expected location.
    """
    # Define the expected output path for the figure
    figure_path = './figures/affordability_bar_chart.png'

    # Assert that the figure file exists at the specified location
    assert os.path.exists(figure_path), f"Figure not found at {figure_path}"
