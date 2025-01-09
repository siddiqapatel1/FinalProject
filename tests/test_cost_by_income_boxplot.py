import pandas as pd

# Test 1: Ensure critical columns are present in the merged dataset
def test_critical_columns_exist():
    """
    Test to verify that all required columns for creating the boxplot exist
    in the merged dataset. Missing columns will result in a failed test
    with an appropriate error message.
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load the main data sheet and metadata sheet
    main_data = pd.read_excel(data_path, sheet_name='Data')
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')

    # Merge the datasets to include income groups
    merged_data = pd.merge(
        main_data, 
        country_metadata, 
        left_on='Country Name', 
        right_on='Table Name', 
        how='left'
    )

    # Define the required columns
    required_columns = [
        'Income Group', 
        'Cost of an energy sufficient diet', 
        'Cost of a nutrient adequate diet', 
        'Cost of a healthy diet'
    ]

    # Check if each required column is present in the merged dataset
    for column in required_columns:
        assert column in merged_data.columns, f"Column '{column}' is missing from the merged dataset"

# Test 2: Validate the filtered data used for the boxplot
def test_boxplot_data_validity():
    """
    Test to ensure the filtered data for the boxplot is valid:
    - No missing values in 'Income Group' or 'Cost' columns.
    - Data is properly reshaped and contains valid entries for all diet types.
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load the main data sheet and metadata sheet
    main_data = pd.read_excel(data_path, sheet_name='Data')
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')

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
        value_vars=[
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet'
        ],
        var_name='Diet Type',
        value_name='Cost'
    )

    # Drop rows with missing values in critical columns
    filtered_data = filtered_data.dropna(subset=['Income Group', 'Cost'])

    # Validate that no missing values exist in the filtered data
    assert not filtered_data.isnull().values.any(), "Filtered data contains missing values"

    # Validate that all diet types are present in the reshaped data
    expected_diet_types = [
        'Cost of an energy sufficient diet', 
        'Cost of a nutrient adequate diet', 
        'Cost of a healthy diet'
    ]
    unique_diet_types = filtered_data['Diet Type'].unique()
    for diet in expected_diet_types:
        assert diet in unique_diet_types, f"Diet type '{diet}' is missing from the filtered data"

# Test 3: Validate data ranges for cost values
def test_cost_values_within_expected_range():
    """
    Test to verify that the cost values in the filtered data fall within a 
    reasonable range (e.g., positive values).
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load the main data sheet and metadata sheet
    main_data = pd.read_excel(data_path, sheet_name='Data')
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')

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
        value_vars=[
            'Cost of an energy sufficient diet',
            'Cost of a nutrient adequate diet',
            'Cost of a healthy diet'
        ],
        var_name='Diet Type',
        value_name='Cost'
    )

    # Drop rows with missing values in critical columns
    filtered_data = filtered_data.dropna(subset=['Income Group', 'Cost'])

    # Assert that all cost values are positive
    assert (filtered_data['Cost'] > 0).all(), "Filtered data contains non-positive cost values"
