import pandas as pd

def test_income_group_column_exists():
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load data
    main_data = pd.read_excel(data_path, sheet_name='Data')
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    merged_data = pd.merge(main_data, country_metadata, left_on='Country Name', right_on='Table Name', how='left')

    # Check if "Income Group" column exists
    assert 'Income Group' in merged_data.columns, "Income Group column is missing from the merged dataset"

import os

def test_visualization_file_exists():
    # Run the visualization script (assuming it generates the file)
    os.system("python ./scripts/data_exploration.py")

    # Check if the figure exists
    figure_path = './figures/cost_by_income_group.png'
    assert os.path.exists(figure_path), f"Visualization file not found at {figure_path}"
