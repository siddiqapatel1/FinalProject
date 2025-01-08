import pandas as pd

# Test for critical columns in the merged dataset
def test_critical_columns_exist():
    data_path = './data/Food_Prices_For_Nutrition.xlsx'
    main_data = pd.read_excel(data_path, sheet_name='Data')
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    merged_data = pd.merge(main_data, country_metadata, left_on='Country Name', right_on='Table Name', how='left')
    required_columns = ['Income Group', 'Cost of an energy sufficient diet', 'Cost of a nutrient adequate diet', 'Cost of a healthy diet']
    for column in required_columns:
        assert column in merged_data.columns, f"Column {column} is missing from the merged dataset"

# Test for validity of boxplot data
def test_boxplot_data_validity():
    data_path = './data/Food_Prices_For_Nutrition.xlsx'
    main_data = pd.read_excel(data_path, sheet_name='Data')
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    merged_data = pd.merge(main_data, country_metadata, left_on='Country Name', right_on='Table Name', how='left')
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
    filtered_data = filtered_data.dropna(subset=['Income Group', 'Cost'])
    assert not filtered_data.isnull().values.any(), "Filtered data contains missing values"
