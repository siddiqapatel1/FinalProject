import pandas as pd
import os

def test_required_columns_exist():
    """
    Test if the required columns for summary statistics exist in the dataset.

    This test ensures that all necessary columns for calculating diet costs 
    and affordability statistics are present in the dataset. If any column 
    is missing, the test will fail and indicate which column is missing.
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'
    
    # Load the main data sheet
    main_data = pd.read_excel(data_path, sheet_name='Data')
    
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
        assert column in main_data.columns, f"Missing column: {column}"

def test_summary_statistics_calculations():
    """
    Test if the summary statistics for diet costs are calculated correctly.

    This test uses a mock dataset to calculate summary statistics and verifies
    that the mean values for each diet cost type match the expected results.
    """
    # Mock data representing diet costs
    data = {
        'Cost of an energy sufficient diet': [0.5, 1.0, 1.5],
        'Cost of a nutrient adequate diet': [2.0, 2.5, 3.0],
        'Cost of a healthy diet': [3.5, 4.0, 4.5]
    }
    df = pd.DataFrame(data)
    
    # Calculate summary statistics
    stats = df.describe()
    
    # Assert that the calculated mean values match the expected results
    assert stats.loc['mean', 'Cost of an energy sufficient diet'] == 1.0
    assert stats.loc['mean', 'Cost of a nutrient adequate diet'] == 2.5
    assert stats.loc['mean', 'Cost of a healthy diet'] == 4.0

def test_cost_ratios():
    """
    Test if cost ratios (Healthy vs Energy Sufficient, Healthy vs Nutrient Adequate)
    are calculated correctly.

    This test verifies that the calculated cost ratios for mock data match 
    the expected values.
    """
    # Mock data representing diet costs
    data = {
        'Cost of an energy sufficient diet': [0.5, 1.0],
        'Cost of a nutrient adequate diet': [2.0, 2.5],
        'Cost of a healthy diet': [3.5, 4.0]
    }
    df = pd.DataFrame(data)
    
    # Calculate cost ratios
    df['Healthy vs Energy Sufficient'] = df['Cost of a healthy diet'] / df['Cost of an energy sufficient diet']
    df['Healthy vs Nutrient Adequate'] = df['Cost of a healthy diet'] / df['Cost of a nutrient adequate diet']
    
    # Assert that the calculated ratios match the expected values
    assert df['Healthy vs Energy Sufficient'].iloc[0] == 7.0
    assert df['Healthy vs Nutrient Adequate'].iloc[1] == 1.6

def test_output_files():
    """
    Test if summary statistics CSV files are saved in the correct folder.

    This test ensures that the output files containing summary statistics 
    are generated and saved in the './summary_stats_results/' folder.
    """
    # Define the expected file paths
    expected_files = [
        './summary_stats_results/diet_cost_summary.csv',
        './summary_stats_results/affordability_summary.csv',
        './summary_stats_results/cost_ratios_summary.csv'
    ]
    
    # Assert that each file exists in the expected folder
    for file_path in expected_files:
        assert os.path.exists(file_path), f"Output file not found: {file_path}"
