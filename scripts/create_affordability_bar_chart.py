import pandas as pd
import matplotlib.pyplot as plt

# Path to the dataset
data_path = './data/Food_Prices_For_Nutrition.xlsx'

try:
    # Step 1: Load the dataset
    # Load the main data sheet containing affordability metrics
    main_data = pd.read_excel(data_path, sheet_name='Data')

    # Load the metadata sheet containing income group and region classifications
    country_metadata = pd.read_excel(data_path, sheet_name='Country - Metadata')

    # Step 2: Merge data and filter required columns
    # Merge the main data with metadata on country names
    merged_data = pd.merge(
        main_data,
        country_metadata,
        left_on='Country Name',
        right_on='Table Name',
        how='left'
    )

    # Extract relevant columns for affordability analysis
    affordability_data = merged_data[['Country Name', 'Income Group', 'Percent of the population who cannot afford sufficient calories','Percent of the population who cannot afford nutrient adequacy', 'Percent of the population who cannot afford a healthy diet']]

    # Rename columns for clarity and readability
    affordability_data.columns = ['Country', 'Income Group', 'Energy Sufficient Diet','Nutrient Adequate Diet', 'Healthy Diet']

    # Step 3: Filter and reorder data for the chart
    # Specify the order of countries and regions for the plot
    ordered_countries = [
        "East Asia & Pacific", "Europe & Central Asia", "Latin America & Caribbean",
        "Middle East & North Africa", "North America", "South Asia", "Sub-Saharan Africa",
        "WORLD", "High income", "Upper-middle income", "Lower-middle income", "Low income"
    ]
    # Filter and reorder data based on the specified order
    affordability_data = affordability_data[affordability_data['Country'].isin(ordered_countries)]
    affordability_data = affordability_data.set_index('Country').reindex(ordered_countries)

    # Step 4: Create the plot
    # Define diet types and corresponding colors for the bar chart
    diet_types = ['Energy Sufficient Diet', 'Nutrient Adequate Diet', 'Healthy Diet']
    colours = ['#88CCEE', '#DDCC77', '#117733']  # Light color-blind-friendly palette

    # Create a horizontal bar chart with subplots for each diet type
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 8), sharey=True)

    for i, diet in enumerate(diet_types):
        ax = axes[i]
        # Plot the horizontal bar chart
        ax.barh(affordability_data.index, affordability_data[diet], color=colours[i])
        ax.set_title(diet, fontsize=16, fontweight='bold', pad=15)  # Add title to each subplot
        ax.set_xlim(0, 100)  # Set x-axis limits to percentage values

        # Add percentage labels to each bar
        for index, value in enumerate(affordability_data[diet]):
            ax.text(value + 2, index, f"{value:.1f}%", va='center', fontsize=15, color='black', fontweight = 'bold')

        # Remove unnecessary spines and grid lines for a cleaner look
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.grid(False)

        # Hide y-axis labels for all but the first subplot
        if i > 0:
            ax.tick_params(left=False)

    # Step 5: Add shared labels and adjust layout
    # Set shared y-axis labels for country names
    axes[0].set_yticklabels(affordability_data.index, fontsize=14, fontweight = 'bold')
    axes[0].tick_params(axis='y', labelsize=14)

    # Add a shared x-axis label centered across all subplots
    fig.text(0.5, 0.02, 'Percentage of Population (%)', ha='center', fontsize=14,fontweight='bold')

    # Add a shared title for the entire figure
    fig.suptitle('Share of Population Unable to Afford Different Diet Standards, 2021', 
                 fontsize=20, fontweight='bold', y=1.02)

    # Adjust the layout for better spacing
    plt.tight_layout(w_pad=3, rect=[0, 0.05, 1, 0.95])  # Add space at the top for the title

    # Step 6: Save and display the figure
    # Save the final plot as a PNG file
    plt.savefig('./figures/affordability_bar_chart.png', bbox_inches='tight')
    print("Figure saved to './figures/population_affordability_bar_chart.png'")

    plt.show()

except Exception as e:
    # Handle any exceptions that occur during data loading or plotting
    print(f"Error: {e}")
