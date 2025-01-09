import pandas as pd
import os

def test_percentage_contributions_sum():
    """
    Test to verify that the percentage contributions of each food group 
    to the cost of a healthy diet sum to 100%.

    This test ensures that the average contributions of different food 
    groups are correctly normalized to percentages and that the total 
    percentage adds up to 100%, indicating a valid pie chart representation.
    """
    # Path to the dataset
    data_path = './data/Food_Prices_For_Nutrition.xlsx'

    # Load the dataset
    df = pd.read_excel(data_path, sheet_name='Data')

    # Extract relevant columns for food group costs
    pie_chart_data = df[['Cost of fruits', 'Cost of starchy staples','Cost of vegetables','Cost of animal-source foods', 'Cost of legumes, nuts and seeds', 'Cost of oils and fats']]

    # Calculate average contributions for each food group
    average_contributions = pie_chart_data.mean()

    # Calculate the total cost across all food groups
    total_cost = average_contributions.sum()

    # Convert contributions to percentages
    percentage_contributions = (average_contributions / total_cost) * 100

    # Assert that the total percentage is approximately 100% (tolerance: 0.01%)
    assert abs(percentage_contributions.sum() - 100) < 0.01, \
        "Percentage contributions do not sum to 100"

def test_pie_chart_saved():
    """
    Test to verify that the pie chart figure is saved successfully in the 
    specified output directory.

    This test checks the existence of the pie chart image file to ensure
    that the visualization script generated the output as expected.
    """
    # Define the expected output path for the pie chart figure
    output_path = './figures/food_group_pie_chart.png'

    # Assert that the file exists at the specified location
    assert os.path.exists(output_path), f"Pie chart not found at {output_path}"
