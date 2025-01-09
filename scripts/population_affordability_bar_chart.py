import pandas as pd
import matplotlib.pyplot as plt

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
    affordability_data = merged_data[['Country Name', 'Income Group','Percent of the population who cannot afford sufficient calories','Percent of the population who cannot afford nutrient adequacy', 'Percent of the population who cannot afford a healthy diet']]

    # Rename columns for clarity
    affordability_data.columns = ['Country', 'Income Group', 'Energy Sufficient Diet','Nutrient Adequate Diet', 'Healthy Diet']

    # Filter and reorder data 
    ordered_countries = [
        "East Asia & Pacific", "Europe & Central Asia", "Latin America & Caribbean",
        "Middle East & North Africa", "North America", "South Asia", "Sub-Saharan Africa",
        "WORLD", "High income", "Upper-middle income", "Lower-middle income", "Low income"
    ]
    affordability_data = affordability_data[affordability_data['Country'].isin(ordered_countries)]
    affordability_data = affordability_data.set_index('Country').reindex(ordered_countries)

    # Create horizontal bar charts for each diet type
    diet_types = ['Energy Sufficient Diet', 'Nutrient Adequate Diet', 'Healthy Diet']
    colours = ['#88CCEE', '#DDCC77', '#117733']  # Light colour-blind-friendly palette

     # Create horizontal bar charts for each diet type
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 8), sharey=True)

    for i, diet in enumerate(diet_types):
        ax = axes[i]
        ax.barh(affordability_data.index, affordability_data[diet], color=colours[i])
        ax.set_title(diet, fontsize=16, pad=15)
        ax.set_xlim(0, 100)

        # Add percentages to bars
        for index, value in enumerate(affordability_data[diet]):
            ax.text(value + 2, index, f"{value:.1f}%", va='center', fontsize=12, color='black')

        # Remove all spines and grid lines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.grid(False)

        # Hide y-axis labels for all but the first subplot
        if i > 0:
            ax.tick_params(left=False)

    # Set shared y-axis labels (country names)
    axes[0].set_yticklabels(affordability_data.index, fontsize=14)
    axes[0].tick_params(axis='y', labelsize=14)

    # Add a single x-axis label centered across all subplots
    fig.text(0.5, 0.02, 'Percentage of Population (%)', ha='center', fontsize=14)

    # Adjust layout
    plt.tight_layout(w_pad=3, rect=[0, 0.05, 1, 1])  # Add space at the bottom for the label

    # Save the figure
    plt.savefig('./figures/population_affordability_bar_chart', bbox_inches='tight')
    print("Figure saved to './figures/population_affordability_bar_chart.png'")


except Exception as e:
    print(f"Error: {e}")
