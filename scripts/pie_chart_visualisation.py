import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to the dataset
data_path = './data/Food_Prices_For_Nutrition.xlsx'

try:
    # Load the main data sheet
    main_data = pd.read_excel(data_path, sheet_name='Data')
    
    # Load the country metadata sheet for income group and region
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')
    
    # Merge the main dataset with country metadata
    merged_data = pd.merge(
        main_data, 
        country_metadata, 
        left_on='Country Name', 
        right_on='Table Name', 
        how='left'
    )
    
    # Select relevant columns
    affordability_data = merged_data[['Income Group', 
                                      'Percent of the population who cannot afford sufficient calories',
                                      'Percent of the population who cannot afford nutrient adequacy',
                                      'Percent of the population who cannot afford a healthy diet']]

    # Drop rows with missing Income Group
    affordability_data = affordability_data.dropna(subset=['Income Group'])

    # Group data by Income Group and calculate the mean for each diet type
    grouped_data = affordability_data.groupby('Income Group').mean()

    # Prepare data for the stacked bar chart
    diet_types = ['Percent of the population who cannot afford sufficient calories',
                  'Percent of the population who cannot afford nutrient adequacy',
                  'Percent of the population who cannot afford a healthy diet']

    # Rename diet types for better readability
    diet_labels = ['Energy Sufficient Diet', 'Nutrient Adequate Diet', 'Healthy Diet']
    percentages = [grouped_data[diet] for diet in diet_types]

    # Create the stacked bar chart
    plt.figure(figsize=(10, 6))
    x = grouped_data.index  # Income Groups
    bottom = np.zeros(len(x))

    for i, (percent, label) in enumerate(zip(percentages, diet_labels)):
        plt.bar(x, percent, bottom=bottom, label=label)
        bottom += percent

    # Add chart details
    plt.title('Percentage of Population Unable to Afford Diets by Income Group', fontsize=16)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.xlabel('Income Group', fontsize=12)
    plt.legend(title='Diet Type', fontsize=10)
    plt.xticks(rotation=30)
    plt.tight_layout()

    # Save the figure
    plt.savefig('./figures/population_affordability_by_income_group.png')
    print("Figure saved to './figures/population_affordability_by_income_group.png'")

except Exception as e:
    print(f"Error: {e}")
