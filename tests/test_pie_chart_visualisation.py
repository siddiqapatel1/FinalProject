import pandas as pd

def test_percentage_contributions_sum():
    data_path = './data/Food_Prices_For_Nutrition.xlsx'
    df = pd.read_excel(data_path, sheet_name='Data')

    # Extract relevant columns
    pie_chart_data = df[['Cost of fruits', 'Cost of starchy staples', 'Cost of vegetables','Cost of animal-source foods', 'Cost of legumes, nuts and seeds', 'Cost of oils and fats']]
    average_contributions = pie_chart_data.mean()
    total_cost = average_contributions.sum()
    percentage_contributions = (average_contributions / total_cost) * 100

    # Assert that the percentages sum to 100
    assert abs(percentage_contributions.sum() - 100) < 0.01, "Percentage contributions do not sum to 100"


import os

def test_pie_chart_saved():
    # Path where the figure should be saved
    output_path = './figures/food_group_pie_chart.png'

    # Check if the figure file exists
    assert os.path.exists(output_path), f"Pie chart not found at {output_path}"


