#Test 1: Verify Required Columns

import pandas as pd

def test_required_columns_exist():
    data_path = './data/Food_Prices_For_Nutrition.xlsx'
    df = pd.read_excel(data_path, sheet_name='Data')

    required_columns = [
        'Country Name',
        'Percent of the population who cannot afford sufficient calories',
        'Percent of the population who cannot afford nutrient adequacy',
        'Percent of the population who cannot afford a healthy diet'
    ]
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

#Test2: Verify Data Filtering for the Visualisation
import pandas as pd

def test_data_filtering():
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'
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
    assert filtered_data['Income Group'].isnull().sum() == 0, "Filtered data contains rows with null Income Group"

#Test3: Verify figure output

import os

def test_figure_saved():
    figure_path = './figures/population_affordability_bar_chart.png'
    assert os.path.exists(figure_path), f"Figure not found at {figure_path}"


